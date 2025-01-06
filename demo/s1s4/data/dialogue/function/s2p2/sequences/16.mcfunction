tellraw @a ["", {"text": "你", "color": "#94abff"}, "：是呀！"]

scoreboard players set next_dialogue_id Dialogue.Global 17
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 40
scoreboard players set guard Dialogue.Global 1
