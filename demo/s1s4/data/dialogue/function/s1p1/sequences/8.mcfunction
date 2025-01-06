tellraw @a ["", {"text": "曉澄", "color": "#a1f8c3"}, "：叔叔", {"text": "你", "color": "#94abff"}, "好老喔！"]

scoreboard players set next_dialogue_id Dialogue.Global 9
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 46
scoreboard players set guard Dialogue.Global 1
