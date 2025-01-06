tellraw @a ["", {"text": "寶琳", "color": "#d686ff"}, "：請問……這裡有人嗎？"]

scoreboard players set next_dialogue_id Dialogue.Global 7
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 56
scoreboard players set guard Dialogue.Global 1
