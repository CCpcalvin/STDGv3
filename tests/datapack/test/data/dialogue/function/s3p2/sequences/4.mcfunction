tellraw @a ["[任務：睡覺]"]

scoreboard players set next_dialogue_id Dialogue.Global 5
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 40
scoreboard players set guard Dialogue.Global 1
scoreboard players set pause Dialogue.Global 1
