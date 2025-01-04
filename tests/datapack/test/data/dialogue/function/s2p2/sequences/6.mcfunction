tellraw @a ["", {"text": "嗣尤", "color": "aqua"}, "：有這個想法很不錯嘛~"]

scoreboard players set next_dialogue_id Dialogue.Global 7
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 61
scoreboard players set guard Dialogue.Global 1
