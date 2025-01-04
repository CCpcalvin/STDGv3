from __future__ import annotations

from typing import Optional, TextIO

from .gen import *


class Sequence:
    start_id = START_ID
    default_sequence_interval = DEFAULT_SEQUENCES_INTERVAL

    def __init__(
        self,
        cmd_str: Optional[str] = None,
    ):
        if cmd_str:
            self.cmd_str = cmd_str + "\n"
        else:
            self.cmd_str = None

        self.next: Optional[Sequence] = None
        self.pervious: Optional[Sequence] = None
        self.time_to_next_sequence: Optional[int] = None

    def print_content(self):
        return f"\t CommandString: {self.cmd_str}\n"

    def __str__(self):
        return f"Sequence: \n {self.print_content()}"

    def print_tree_recursive(self, id: int):
        print(id, end=". ")
        print(self)
        if self.next:
            self.next.print_tree_recursive(id + 1)

    def print_tree(self):
        self.print_tree_recursive(self.start_id)

    def get_head(self):
        if self.pervious is not None:
            return self.pervious.get_head()

        else:
            return self

    def get_last(self):
        if self.next is not None:
            return self.next.get_last()

        else:
            return self

    def get_next(self, num: int):
        if num < 0:
            raise Exception("Domain error")

        if num == 0 or not self.next:
            return self

        else:
            return self.next.get_next(num - 1)

    def get_pervious(self, num: int):
        if num < 0:
            raise Exception("Domain error")

        if num == 0 or not self.pervious:
            return self

        else:
            return self.pervious.get_pervious(num - 1)

    def insert_before(self, sequence: Sequence):
        if self.pervious:
            pervious = self.pervious
            pervious.next = sequence
            sequence.pervious = pervious

        sequence.next = self
        self.pervious = sequence

    def insert_after(self, sequence: Sequence):
        if self.next:
            next = self.next
            next.pervious = sequence
            sequence.next = next

        sequence.pervious = self
        self.next = sequence

    def get_cmd(self):
        if not self.cmd_str:
            return ""
        else:
            return self.cmd_str

    def get_time_to_next_sequence(self):
        if not self.time_to_next_sequence:
            self.time_to_next_sequence = self.default_sequence_interval

        return self.time_to_next_sequence

    def generate_sequence(self, id: int, data_path: str, run_sequence_file: TextIO):
        # For generating sequence mcfunction
        cmd = self.get_cmd()
        cmd += set_next_dialogue_id(id + 1)
        cmd += RESET_TIMER_CMD
        cmd += set_time_to_next_sequence(self.get_time_to_next_sequence())
        cmd += SET_GUARD_CMD

        if not self.next:
            cmd += set_pause()

        with open(
            os.path.join(data_path, SEQUENCES_PATH, f"sequence_{id}.mcfunction"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(cmd)

        # For generating run_sequences.mcfunction
        run_sequence_file.write(
            f"execute if score {NEXT_DIALOGUE_ID} {GLOBAL_SCOREBOARD_OBJ} matches {id} if score {SEQUENCE_GUARD} {GLOBAL_SCOREBOARD_OBJ} matches 0 run "
            + run_sequence(id)
            + "\n"
        )

        if self.next:
            self.next.generate_sequence(id + 1, data_path, run_sequence_file)

    def generate_datapack(
        self,
        datapack_path: str,
        datapack_name: str,
        pack_format: int = 61,
        datapack_description: str = "STDGv3",
        reload: bool = False,
    ):
        data_path = create_datapack(
            datapack_path, datapack_name, pack_format, datapack_description, reload
        )
        init_datapack(data_path)

        # Generate sequence functions
        os.makedirs(os.path.join(data_path, SEQUENCES_PATH))
        run_sequences_file = open(
            os.path.join(data_path, RUN_SEQUENCES_FUNCTION_PATH), "w", encoding="utf-8"
        )
        self.generate_sequence(START_ID, data_path, run_sequences_file)
        run_sequences_file.close()

        # Generate start sequence function
        start_cmd = FORCE_RESET_CMD
        start_cmd += stop_pause()
        start_cmd += run_sequence(START_ID)
        with open(
            os.path.join(data_path, SEQUENCES_PATH, f"start.mcfunction"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(start_cmd)
