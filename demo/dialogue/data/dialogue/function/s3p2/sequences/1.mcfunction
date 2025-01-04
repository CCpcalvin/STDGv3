tellraw @a ["你：難道今年注定單身嗎！"]

scoreboard players set next_dialogue_id Dialogue.Global 2
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 56
scoreboard players set guard Dialogue.Global 1
