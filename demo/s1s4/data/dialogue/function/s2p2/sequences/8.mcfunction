tellraw @a ["", {"text": "你", "color": "#94abff"}, "：可是現在我們被無數世界相隔"]

scoreboard players set next_dialogue_id Dialogue.Global 9
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 73
scoreboard players set guard Dialogue.Global 1
