tellraw @a "嗣尤：還掛念她嗎？"
scoreboard players set next_dialogue_id Dialogue.Global 2
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 20
