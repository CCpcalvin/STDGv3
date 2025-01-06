tellraw @a ["", {"text": "雪縈", "color": "#abf7ff"}, "：叫我Yuki就好了"]

scoreboard players set next_dialogue_id Dialogue.Global 8
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 48
scoreboard players set guard Dialogue.Global 1
