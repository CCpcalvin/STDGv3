tellraw @a ["你：明明是劇情向地圖，但硬要我做支線及解謎"]

scoreboard players set next_dialogue_id Dialogue.Global 10
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 101
scoreboard players set guard Dialogue.Global 1
