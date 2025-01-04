tellraw @a ["你：今年也要麻煩你幫忙~ 多多指教囉！"]

scoreboard players set next_dialogue_id Dialogue.Global 16
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 86
scoreboard players set guard Dialogue.Global 1
