tellraw @a ["", {"text": "你", "color": "#94abff"}, "：突然要解謎跟槍戰，一定是這個作者做的"]

scoreboard players set next_dialogue_id Dialogue.Global 12
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 96
scoreboard players set guard Dialogue.Global 1
