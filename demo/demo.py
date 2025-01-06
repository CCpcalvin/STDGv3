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
    scripts_pool = r"C:\Users\spagh\Desktop\Spaghetti Even\Minecraft map\STDGv3\demo\scripts"
    STDGv3.DialogueSequence.update_colormap({
        "你": "#94abff", "嗣尤": "#ffb974", "妹妹": "#ff80f0", "鈺樺": "#ffec8d", "寶琳": "#d686ff", "雪縈": "#abf7ff", "曉澄": "#a1f8c3", "幸姈": "#ffbac6"
    })

    for file in os.listdir(scripts_pool):
        scene = file.split(".")[0]
        head = STDGv3.read_script(os.path.join(scripts_pool, file), scene)
        MissionModifier(head)
        OptionFeedbackModifier(head)
        head.generate_dialogue_json()
        sqDict[scene] = head
    
    sq = sqDict["s1p1"]
    sq.append("function outfit_chiikawa:give")
    sq.search_dialogue_next("嗣尤：你跟她都分手一段時間了").insert_cmd_after(["function outfit_hachiware:give"]).time_to_next_sequence = 10

    sq.search_dialogue_next("嗣尤：你跟她都分手一段時間了").get_time_to_next_sequence()
    sq.get_next(7).insert_cmd_before(["function outfit_usagi:give"])


    sq = sqDict["s2p1"]
    sq.append("function tutorial:give")
    sq.print_tree()

    sq.time_to_next_sequence = 10

    sqList = list(sqDict.values())
    STDGv3.generate_datapack(
        sqList,
        r"C:\Users\spagh\AppData\Roaming\.minecraft\saves\《蛇年愛情妄想症》\datapacks",
        "testing",
        reload=True,
    )


if __name__ == "__main__":
    main()
