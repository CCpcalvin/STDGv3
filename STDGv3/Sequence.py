from .Helper import *
from typing import Optional, TextIO


class Sequence:
    def __init__(
        self,
        id: int,
        cmd_str: Optional[str] = None,
    ):
        self.id: int = id
        self.cmd_str = cmd_str
        self.next: Optional[Sequence] = None
        self.pervious: Optional[Sequence] = None
        self.time_to_next_sequence: Optional[int] = None

    def print_content(self):
        return f"\t ID: {self.id}\n\t CommandString: {self.cmd_str}\n"

    def __str__(self):
        return f"Sequence: \n {self.print_content()}"

    def print_tree(self):
        print(self)
        if self.next:
            self.next.print_tree()

    def get_last(self):
        if self.next is not None:
            return self.next.get_last()

        else:
            return self

    def generate_cmd(self):
        if not self.cmd_str:
            return ""
        else:
            return self.cmd_str

    def generate_interval(self):
        if not self.time_to_next_sequence:
            self.time_to_next_sequence = DEFAULT_SEQUENCES_INTERVAL

        return self.time_to_next_sequence

    def generate_sequence(self, data_path: str, run_sequence_file: TextIO):
        # For generating sequence mcfunction
        cmd = self.generate_cmd()
        cmd += set_next_dialogue_id(self.id + 1)
        cmd += RESET_TIMER_CMD
        cmd += set_time_to_next_sequence(self.generate_interval())
        cmd += SET_GUARD_CMD

        if not self.next:
            cmd += set_pause()

        with open(
            os.path.join(data_path, SEQUENCES_PATH, f"sequence_{self.id}.mcfunction"),
            "w",
        ) as f:
            f.write(cmd)

        # For generating run_sequences.mcfunction
        run_sequence_file.write(
            f"execute if score {NEXT_DIALOGUE_ID} {GLOBAL_SCOREBOARD_OBJ} matches {self.id} if score {SEQUENCE_GUARD} {GLOBAL_SCOREBOARD_OBJ} matches 0 run "
            + run_sequence(self.id)
            + "\n"
        )

        if self.next:
            self.next.generate_sequence(data_path, run_sequence_file)

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
            os.path.join(data_path, RUN_SEQUENCES_FUNCTION_PATH), "w"
        )
        self.generate_sequence(data_path, run_sequences_file)
        run_sequences_file.close()

        # Generate start sequence function
        start_cmd = FORCE_RESET_CMD
        start_cmd += stop_pause()
        start_cmd += run_sequence(0)
        with open(
            os.path.join(data_path, SEQUENCES_PATH, f"start.mcfunction"),
            "w",
        ) as f:
            f.write(start_cmd)


class DialogueSequence(Sequence):
    def __init__(self, id: int, dialogue_str: str):
        super().__init__(id)
        self.dialogue_str = dialogue_str.strip()

    def print_content(self):
        return f"{super().print_content()}\t DialogueString: {self.dialogue_str}\n"

    def __str__(self):
        return f"Dialogue Sequence: \n {self.print_content()}\t\n"

    def generate_cmd(self):
        self.cmd_str = f'tellraw @a "{self.dialogue_str}"\n'
        return self.cmd_str
