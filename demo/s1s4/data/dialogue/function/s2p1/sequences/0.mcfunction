function s2p1:1
scoreboard players set next_dialogue_id Dialogue.Global 1
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 60
scoreboard players set guard Dialogue.Global 1
