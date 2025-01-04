tellraw @a ["", {"text": "嗣尤", "color": "aqua"}, "：你還真的是痴撚線【瘋掉了】！"]

scoreboard players set next_dialogue_id Dialogue.Global 18
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 76
scoreboard players set guard Dialogue.Global 1
scoreboard players set pause Dialogue.Global 1
