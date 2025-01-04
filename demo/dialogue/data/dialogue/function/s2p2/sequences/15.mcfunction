tellraw @a ["你：是呀！"]

scoreboard players set next_dialogue_id Dialogue.Global 16
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 40
scoreboard players set guard Dialogue.Global 1
