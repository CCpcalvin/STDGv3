function dialogue:s2p1/start
scoreboard players set next_dialogue_id Dialogue.Global 4
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 20
scoreboard players set guard Dialogue.Global 1
