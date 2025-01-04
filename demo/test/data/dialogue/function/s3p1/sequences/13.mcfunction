tellraw @a ["你：別誤會！我回復單身都不覺荒涼"]

scoreboard players set next_dialogue_id Dialogue.Global 14
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 76
scoreboard players set guard Dialogue.Global 1
