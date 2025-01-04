tellraw @a ["你：不論你上次選了哪個結局也好"]

scoreboard players set next_dialogue_id Dialogue.Global 7
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 73
scoreboard players set guard Dialogue.Global 1
