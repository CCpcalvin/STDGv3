tellraw @a ["", {"text": "嗣尤", "color": "aqua"}, "：還掛念她嗎？"]

scoreboard players set next_dialogue_id Dialogue.Global 2
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 41
scoreboard players set guard Dialogue.Global 1
