tellraw @a ["", {"text": "你", "color": "#94abff"}, "：現在我都被分手，回復單身了"]

scoreboard players set next_dialogue_id Dialogue.Global 8
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 71
scoreboard players set guard Dialogue.Global 1
