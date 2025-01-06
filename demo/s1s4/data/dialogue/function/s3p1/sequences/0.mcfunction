tellraw @a ["", {"text": "你", "color": "#94abff"}, "：Zzzzzz…"]

scoreboard players set next_dialogue_id Dialogue.Global 1
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 40
scoreboard players set guard Dialogue.Global 1
