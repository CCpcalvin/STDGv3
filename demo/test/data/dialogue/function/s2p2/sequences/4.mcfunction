tellraw @a ["你：我可不像你，有這麼多人追求呢！"]

scoreboard players set next_dialogue_id Dialogue.Global 5
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 78
scoreboard players set guard Dialogue.Global 1
