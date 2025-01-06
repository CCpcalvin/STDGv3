tellraw @a ["???：可能我們是兩個世界的人"]

scoreboard players set next_dialogue_id Dialogue.Global 3
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 66
scoreboard players set guard Dialogue.Global 1
