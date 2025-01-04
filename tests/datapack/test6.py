import re
from typing import Dict, List

import STDGv3


def add_color(json: List[Dict], keyword: str, color: str):
    for i, json_elem in enumerate(json):
        str_list = re.split(f"({keyword})", json_elem["text"])
        for str_elem in str_list:
            if str_elem == keyword:
                json[i] = {"text": str_elem, "color": color}


def Str2Json(text: str, colormap: Dict[str, str] = {}):
    for keyword in colormap:
        pass


def test():
    # colormap = {"嗣尤": "aqua", "幸姈": "red"}
    colormap = {}
    pattern = re.compile("(" + "|".join(colormap.keys()) + ")")

    text = "嗣尤：幸姈還真的是痴撚線【瘋掉了】！"
    text_list = re.split(pattern, text)

    for i, text_elem in enumerate(text_list):
        if text_elem in colormap:
            text_list[i] = {"text": text_elem, "color": colormap[text_elem]}

    print(text_list)


def main():
    head = STDGv3.read_script("./tests/datapack/scripts.txt")
    STDGv3.DialogueSequence.update_colormap({"嗣尤": "aqua", "幸姈": "red"})
    head.generate_dialogue_json()

    head.print_tree()
    head.generate_datapack("./tests/datapack/", "test", reload=True)


if __name__ == "__main__":
    # test()
    main()
