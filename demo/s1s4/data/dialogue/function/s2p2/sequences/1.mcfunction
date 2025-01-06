tellraw @a ["", {"text": "嗣尤", "color": "#ffb974"}, "：", {"text": "你", "color": "#94abff"}, "跟她都分手一段時間了"]

scoreboard players set next_dialogue_id Dialogue.Global 2
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 10
scoreboard players set guard Dialogue.Global 1
