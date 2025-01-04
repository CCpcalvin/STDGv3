from .Sequence import Sequence


import re
import math

from .gen import *


def count_chinese_characters(text: str):
    # Define a regular expression pattern for Chinese characters
    chinese_char_pattern = r"[\u4e00-\u9fff]"

    # Use re.findall to find all Chinese characters in the text
    chinese_chars = re.findall(chinese_char_pattern, text)

    # Return the count of Chinese characters
    return len(chinese_chars)


class DialogueSequence(Sequence):
    chinese_character_reading_speed = 4.0
    english_character_reading_speed = 100 * 4.7 / 60

    def __init__(self, dialogue_str: str):
        super().__init__()
        self.dialogue_str = dialogue_str.strip()

    def print_content(self):
        return f"{super().print_content()}\t DialogueString: {self.dialogue_str}\n"

    def __str__(self):
        return f"Dialogue Sequence: \n {self.print_content()}\t\n"

    def get_cmd(self):
        if not self.cmd_str:
            self.cmd_str = f'tellraw @a "{self.dialogue_str}"\n'

        return self.cmd_str

    def compute_time_to_next_sequence(self):
        chin_char_num = count_chinese_characters(self.dialogue_str)
        eng_char_num = len(self.dialogue_str) - chin_char_num

        self.time_to_next_sequence = math.ceil(
            (
                chin_char_num / self.chinese_character_reading_speed
                + eng_char_num / self.english_character_reading_speed
            )
            * TICK_PER_SECOND
        )

    def get_time_to_next_sequence(self):
        if not self.time_to_next_sequence:
            self.compute_time_to_next_sequence()

        return self.time_to_next_sequence
