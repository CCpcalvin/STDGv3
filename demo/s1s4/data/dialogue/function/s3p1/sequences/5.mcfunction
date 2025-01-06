tellraw @a ["", {"text": "你", "color": "#94abff"}, "：「怎麼還是這樣懶慵慵的？」"]

scoreboard players set next_dialogue_id Dialogue.Global 6
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 66
scoreboard players set guard Dialogue.Global 1
