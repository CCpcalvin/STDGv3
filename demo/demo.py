import os
import re

import STDGv3


def MissionModifier(head):
    if isinstance(head, STDGv3.DialogueSequence):
        pattern = r"\[任務(.*)\]"
        if re.search(pattern, head.dialogue_str):
            head.dialogue_cmd_json = [{"text": head.dialogue_str, "color": "green"}]
            head.append(
                "execute as @a at @s run playsound minecraft:entity.player.levelup player @s ~ ~ ~"
            )

    if head.next:
        MissionModifier(head.next)


def OptionFeedbackModifier(head):
    if isinstance(head, STDGv3.DialogueSequence):
        pattern = r"你選擇了(.*)"
        if re.search(pattern, head.dialogue_str):
            head.dialogue_cmd_json = [{"text": head.dialogue_str, "color": "green"}]
            head.append(
                "execute as @a at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~"
            )

    if head.next:
        OptionFeedbackModifier(head.next)


def main():
    sqDict: dict[str, STDGv3.Sequence] = {}
    scripts_pool = r"demo/scripts"
    STDGv3.DialogueSequence.update_colormap(
        {
            "你": "#94abff",
            "嗣尤": "#ffb974",
            "妹妹": "#ff80f0",
            "鈺樺": "#ffec8d",
            "寶琳": "#d686ff",
            "雪縈": "#abf7ff",
            "曉澄": "#a1f8c3",
            "幸姈": "#ffbac6",
        }
    )

    for file in os.listdir(scripts_pool):
        scene = file.split(".")[0]
        head = STDGv3.read_script(os.path.join(scripts_pool, file), scene)
        MissionModifier(head)
        OptionFeedbackModifier(head)
        head.generate_dialogue_json()
        sqDict[scene] = head

    sq = sqDict["s1p1"]
    sq.insert_cmd_before(["function s1p1:1"]).time_to_next_sequence = 20
    sq.get_next(2).insert_cmd_after(
        ["function dialogue:s2p1/start"]
    ).time_to_next_sequence = 20
    head = head.get_head()

    sq = sqDict["s2p1"]
    sq.insert_cmd_before(["function s2p1:1"]).time_to_next_sequence = 60
    sq.insert_cmd_before(["function s2p1:2"]).time_to_next_sequence = 80
    sq.append("function s2p1:3")

    sq = sqDict["s2p2"]
    sq.insert_cmd_before(["function s2p2:1"]).time_to_next_sequence = 10
    sqFound = sq.search_dialogue_next("嗣尤：你還真的是痴撚線【瘋掉了】！")
    print(sqFound)
    sqFound.insert_cmd_before(["say hi"]).time_to_next_sequence = 10

    print(sq.search_dialogue_next("嗣尤：你還真的是痴撚線【瘋掉了】！"))
    sq.search_dialogue_next("嗣尤：你還真的是痴撚線【瘋掉了】！").insert_cmd_after(
        ["function dialogue:s3p1/start"]
    ).time_to_next_sequence = 10

    sq.time_to_next_sequence = 10

    sqList = list(sqDict.values())
    STDGv3.generate_datapack(
        sqList,
        r"./demo",
        "s1s4",
        reload=True,
    )


if __name__ == "__main__":
    main()
