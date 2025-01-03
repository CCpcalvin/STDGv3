tellraw @a "嗣尤：……"
scoreboard players set next_dialogue_id Dialogue.Global 17
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 20
