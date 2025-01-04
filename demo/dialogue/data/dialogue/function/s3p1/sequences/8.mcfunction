tellraw @a ["你：都怪《現代賤俠2》在上年推出！"]

scoreboard players set next_dialogue_id Dialogue.Global 9
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 73
scoreboard players set guard Dialogue.Global 1
