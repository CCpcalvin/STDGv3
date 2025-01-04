tellraw @a ["你：怎麼感覺有人在看著我……"]

scoreboard players set next_dialogue_id Dialogue.Global 2
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 63
scoreboard players set guard Dialogue.Global 1
