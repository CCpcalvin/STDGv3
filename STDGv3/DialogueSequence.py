import copy
import math
import re
from typing import Dict, List, Optional, Callable, Pattern

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
    color_map: Dict[str, str] = {}
    pattern: Optional[Pattern[str]] = None

    def __init__(self, scene: str, dialogue_str: str):
        super().__init__(scene)
        self.dialogue_str = dialogue_str.strip()
        self.dialogue_cmd_json: Optional[List] = None

    def print_content(self):
        str = super().print_content()
        str += f"\t Dialogue String: {self.dialogue_str}\n"
        str += f"\t Dialogue Command JSON: {self.dialogue_cmd_json}\n"
        return str

    def __str__(self):
        return f"Dialogue Sequence: \n {self.print_content()}\t\n"

    @classmethod
    def update_colormap(cls, color_map: Dict[str, str]):
        cls.color_map = color_map

        if cls.color_map != {}:
            cls.pattern = re.compile("(" + "|".join(cls.color_map.keys()) + ")")
        else:
            cls.pattern = None

    def search_dialogue_next(self, pattern: str):
        if self.next:
            if re.search(pattern, self.dialogue_str):
                return self.next

            return self.next.search_dialogue_next(pattern)

    def generate_dialogue_json(self):
        if not self.dialogue_cmd_json:
            if self.pattern is not None:
                text_list = re.split(self.pattern, self.dialogue_str)
                for i, text_elem in enumerate(text_list):
                    if text_elem in self.color_map:
                        text_list[i] = {
                            "text": text_elem,
                            "color": self.color_map[text_elem],
                        }

                self.dialogue_cmd_json = text_list

            else:
                self.dialogue_cmd_json = [{"text": self.dialogue_str}]

        if self.next:
            self.next.generate_dialogue_json()

    def get_dialogue_cmd(self):
        if not self.dialogue_cmd_json:
            return f'tellraw @a "{self.dialogue_str}"\n'

        return f"tellraw @a {json.dumps(self.dialogue_cmd_json, ensure_ascii=False)}\n"

    def get_cmd_list(self):
        cmd_list = copy.deepcopy(self.cmd_str_list)
        cmd_list.append(self.get_dialogue_cmd())
        return cmd_list

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
