tellraw @a ["", {"text": "嗣尤", "color": "#ffb974"}, "：那", {"text": "你", "color": "#94abff"}, "最近有新對象嗎？"]

scoreboard players set next_dialogue_id Dialogue.Global 4
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 61
scoreboard players set guard Dialogue.Global 1
