tellraw @a ["", {"text": "你", "color": "#94abff"}, "：我知道", {"text": "你", "color": "#94abff"}, "在想甚麼的"]

scoreboard players set next_dialogue_id Dialogue.Global 4
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 53
scoreboard players set guard Dialogue.Global 1
