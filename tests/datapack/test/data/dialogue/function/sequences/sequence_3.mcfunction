tellraw @a "嗣尤：還掛念她嗎？"
scoreboard players set next_dialogue_id Dialogue.Global 4
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 20
scoreboard players set guard Dialogue.Global 1
scoreboard players set pause Dialogue.Global 1
