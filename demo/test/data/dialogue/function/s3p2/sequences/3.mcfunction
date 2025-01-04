tellraw @a ["你：明天還要上班，還是先睡覺了"]

scoreboard players set next_dialogue_id Dialogue.Global 4
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 71
scoreboard players set guard Dialogue.Global 1
