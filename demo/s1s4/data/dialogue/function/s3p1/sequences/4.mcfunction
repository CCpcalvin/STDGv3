tellraw @a ["", {"text": "你", "color": "#94abff"}, "：「兩年前不是玩了《兔年愛情通行證》嗎？」"]

scoreboard players set next_dialogue_id Dialogue.Global 5
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 96
scoreboard players set guard Dialogue.Global 1
