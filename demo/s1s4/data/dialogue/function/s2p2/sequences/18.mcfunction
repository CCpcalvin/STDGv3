tellraw @a ["", {"text": "嗣尤", "color": "#ffb974"}, "：", {"text": "你", "color": "#94abff"}, "還真的是痴撚線【瘋掉了】！"]

scoreboard players set next_dialogue_id Dialogue.Global 19
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 76
scoreboard players set guard Dialogue.Global 1
