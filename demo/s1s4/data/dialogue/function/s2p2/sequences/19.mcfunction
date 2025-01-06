function dialogue:s3p1/start
scoreboard players set next_dialogue_id Dialogue.Global 20
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 10
scoreboard players set guard Dialogue.Global 1
scoreboard players set pause Dialogue.Global 1
