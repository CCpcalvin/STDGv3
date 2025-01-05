import os
import re

import STDGv3


def MissionModifier(head):
    if isinstance(head, STDGv3.DialogueSequence):
        pattern = r"\[(.*)\]"
        if re.search(pattern, head.dialogue_str):
            head.dialogue_cmd_json = [{"text": head.dialogue_str, "color": "green"}]
            head.append(
                "execute as @a at @s run playsound minecraft:entity.player.levelup player @s ~ ~ ~"
            )

    if head.next:
        MissionModifier(head.next)


def main():
    sqList: list[STDGv3.Sequence] = []
    scripts_pool = "./demo/scripts"
    STDGv3.DialogueSequence.update_colormap({"嗣尤": "aqua", "幸姈": "red"})

    for file in os.listdir(scripts_pool):
        scene = file.split(".")[0]
        head = STDGv3.read_script(os.path.join(scripts_pool, file), scene)
        MissionModifier(head)
        head.generate_dialogue_json()
        sqList.append(head)

    STDGv3.generate_datapack(
        sqList,
        "./demo/",
        "dialogue",
        reload=True,
    )


if __name__ == "__main__":
    main()
