tellraw @a ["", {"text": "你", "color": "#94abff"}, "：今年也要麻煩", {"text": "你", "color": "#94abff"}, "幫忙~ 多多指教囉！"]

scoreboard players set next_dialogue_id Dialogue.Global 16
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 86
scoreboard players set guard Dialogue.Global 1
