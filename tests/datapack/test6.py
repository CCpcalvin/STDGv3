import re
from typing import Dict, List

import STDGv3


def main():
    head = STDGv3.read_script("./tests/datapack/scripts.txt")
    STDGv3.DialogueSequence.update_colormap({"嗣尤": "aqua", "幸姈": "red"})
    head.generate_dialogue_json()

    head.print_tree()
    head.generate_datapack("./tests/datapack/", "test", reload=True)


if __name__ == "__main__":
    main()
