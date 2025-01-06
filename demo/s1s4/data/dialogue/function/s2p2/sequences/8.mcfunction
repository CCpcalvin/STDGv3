tellraw @a ["", {"text": "嗣尤", "color": "#ffb974"}, "：？？？"]

scoreboard players set next_dialogue_id Dialogue.Global 9
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 40
scoreboard players set guard Dialogue.Global 1
