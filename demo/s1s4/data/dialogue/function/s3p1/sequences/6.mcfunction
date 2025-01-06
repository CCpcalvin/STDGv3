tellraw @a ["", {"text": "你", "color": "#94abff"}, "：不論", {"text": "你", "color": "#94abff"}, "上次選了哪個結局也好"]

scoreboard players set next_dialogue_id Dialogue.Global 7
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 73
scoreboard players set guard Dialogue.Global 1
