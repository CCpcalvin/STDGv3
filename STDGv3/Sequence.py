from __future__ import annotations

from typing import List, Optional, TextIO

from .gen import *


class Sequence:
    start_id = START_ID
    default_sequence_interval = DEFAULT_SEQUENCES_INTERVAL
    sequence_subpath = SEQUENCES_SUBPATH

    def __init__(
        self,
        scene: str,
        cmd_str_list: Optional[List[str]] = None,
    ):
        if cmd_str_list:
            self.cmd_str_list = cmd_str_list
        else:
            self.cmd_str_list: List[str] = []

        self.next: Optional[Sequence] = None
        self.pervious: Optional[Sequence] = None
        self.time_to_next_sequence: Optional[int] = None

        self.scene = scene
        self.scene_path = os.path.join(FUNCTION_PATH, scene)
        self.scene_sequence_path = os.path.join(self.scene_path, self.sequence_subpath)

    def print_content(self):
        return f"\t CommandString: {self.cmd_str_list}\n\t Time to next Sequence: {self.time_to_next_sequence}\n"

    def __str__(self):
        return f"Sequence: \n {self.print_content()}"

    def print_tree_recursive(self, id: int):
        print(id, end=". ")
        print(self)
        if self.next:
            self.next.print_tree_recursive(id + 1)

    def print_tree(self):
        """Prints out the linked list, used for debugging"""
        self.print_tree_recursive(self.start_id)

    def get_head(self):
        """Gets the head of the linked list"""

        if self.pervious is not None:
            return self.pervious.get_head()

        else:
            return self

    def get_last(self):
        """Gets the last element of the linked list"""

        if self.next is not None:
            return self.next.get_last()

        else:
            return self

    def get_next(self, num: int):
        """
        Gets the next element in the linked list, given the number of elements to traverse.

        Args:
            num (int): The number of elements to traverse.

        Returns:
            Sequence: The next element in the linked list.

        Raises:
            Exception: If num is negative.
        """
        if num < 0:
            raise Exception("Domain error")

        if num == 0 or not self.next:
            return self

        else:
            return self.next.get_next(num - 1)

    def get_pervious(self, num: int):
        """
        Gets the previous element in the linked list, given the number of elements to traverse.

        Args:
            num (int): The number of elements to traverse backward.

        Returns:
            Sequence: The previous element in the linked list.

        Raises:
            Exception: If num is negative.
        """
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

    def get_time_to_next_sequence(self):
        if not self.time_to_next_sequence:
            self.time_to_next_sequence = self.default_sequence_interval

        return self.time_to_next_sequence

    def append(self, cmd: str):
        self.cmd_str_list.append(cmd)

    def extend(self, cmd_list: List[str]):
        self.cmd_str_list.extend(cmd_list)

    def generate_dialogue_json(self):
        if self.next:
            self.next.generate_dialogue_json()

    def get_cmd_list(self):
        return self.cmd_str_list

    def run_sequence(self, id: int):
        return f"function {NAMESPACE}:{self.scene}/{self.sequence_subpath}/{id}\n"

    def generate_sequence(self, id: int, data_path: str, run_sequence_file: TextIO):
        # For generating sequence mcfunction
        with open(
            os.path.join(data_path, self.scene_sequence_path, f"{id}.mcfunction"),
            "w",
            encoding="utf-8",
        ) as f:
            for cmd in self.get_cmd_list():
                f.write(cmd + "\n")

            f.write(set_next_dialogue_id(id + 1))
            f.write(RESET_TIMER_CMD)
            f.write(set_time_to_next_sequence(self.get_time_to_next_sequence()))
            f.write(SET_GUARD_CMD)

            if not self.next:
                f.write(set_pause())

        # For generating run_sequences.mcfunction
        run_sequence_file.write(
            f"execute if score {NEXT_DIALOGUE_ID} {GLOBAL_SCOREBOARD_OBJ} matches {id} if score {SEQUENCE_GUARD} {GLOBAL_SCOREBOARD_OBJ} matches 0 run "
            + self.run_sequence(id)
            + "\n"
        )

        if self.next:
            self.next.generate_sequence(id + 1, data_path, run_sequence_file)

    def get_run_sequence_cmd(self):
        return f"function {NAMESPACE}:{self.scene}/{RUN_SEQUENCES_FUNCTION}\n"

    def generate_entire_sequence(
        self,
        scene_id: int,
        data_path: str,
    ):
        # Generate sequence functions
        os.makedirs(os.path.join(data_path, self.scene_sequence_path))
        run_sequences_file = open(
            os.path.join(
                data_path, self.scene_path, f"{RUN_SEQUENCES_FUNCTION}.mcfunction"
            ),
            "w",
            encoding="utf-8",
        )
        self.generate_sequence(START_ID, data_path, run_sequences_file)
        run_sequences_file.close()

        # Generate start sequence function
        start_cmd = FORCE_RESET_CMD
        start_cmd = set_scene_id(scene_id)
        start_cmd += resume()
        start_cmd += self.run_sequence(START_ID)
        with open(
            os.path.join(data_path, self.scene_path, f"start.mcfunction"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(start_cmd)

        # Generate skip sequence function
        with open(
            os.path.join(data_path, self.scene_path, "skip.mcfunction"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(self.get_run_sequence_cmd())
