tellraw @a ["你：最終我們會跨越時空限制，幸福快樂一起生活！"]

scoreboard players set next_dialogue_id Dialogue.Global 12
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 108
scoreboard players set guard Dialogue.Global 1
