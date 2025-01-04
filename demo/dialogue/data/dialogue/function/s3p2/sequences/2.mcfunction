tellraw @a ["你：嗚嗚~ 越想越傷心"]

scoreboard players set next_dialogue_id Dialogue.Global 3
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 48
scoreboard players set guard Dialogue.Global 1
