tellraw @a "你：沒有啦，都過了這麼久"
scoreboard players set next_dialogue_id Dialogue.Global 3
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 20
