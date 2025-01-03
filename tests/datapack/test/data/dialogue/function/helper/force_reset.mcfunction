function dialogue:helper/reset_timer
scoreboard players set next_dialogue_id Dialogue.Global 0
scoreboard players set pause Dialogue.Global 1
scoreboard players set time_to_next_sequence Dialogue.Global 9999
