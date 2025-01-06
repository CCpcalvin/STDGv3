tellraw @a ["", {"text": "鈺樺", "color": "#ffec8d"}, "：喂，", {"text": "你", "color": "#94abff"}, "別亂說話……"]

scoreboard players set next_dialogue_id Dialogue.Global 6
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 51
scoreboard players set guard Dialogue.Global 1
