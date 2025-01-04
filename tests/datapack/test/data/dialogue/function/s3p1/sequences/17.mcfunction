tellraw @a ["[任務：找到手機]"]

scoreboard players set next_dialogue_id Dialogue.Global 18
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 40
scoreboard players set guard Dialogue.Global 1
scoreboard players set pause Dialogue.Global 1
