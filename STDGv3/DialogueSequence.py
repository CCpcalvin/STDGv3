import math
import re

from .gen import *
from .Sequence import Sequence


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
    min_time_to_next_sequence = 2.0

    def __init__(self, dialogue_str: str):
        super().__init__()
        self.dialogue_str = dialogue_str.strip()

    def print_content(self):
        return f"{super().print_content()}\t DialogueString: {self.dialogue_str}\n"

    def __str__(self):
        return f"Dialogue Sequence: \n {self.print_content()}\t\n"

    def generate_dialogue_cmd(self):
        self.cmd_str_list.append(f'tellraw @a "{self.dialogue_str}"\n')
        if self.next:
            self.next.generate_dialogue_cmd()

    def compute_time_to_next_sequence(self):
        chin_char_num = count_chinese_characters(self.dialogue_str)
        eng_char_num = len(self.dialogue_str) - chin_char_num

        self.time_to_next_sequence = math.ceil(
            max(
                (
                    chin_char_num / self.chinese_character_reading_speed
                    + eng_char_num / self.english_character_reading_speed
                ),
                self.min_time_to_next_sequence,
            )
            * TICK_PER_SECOND
        )

    def get_time_to_next_sequence(self):
        if not self.time_to_next_sequence:
            self.compute_time_to_next_sequence()

        return self.time_to_next_sequence
