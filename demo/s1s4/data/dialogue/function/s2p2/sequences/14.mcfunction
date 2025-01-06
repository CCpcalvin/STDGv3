tellraw @a ["", {"text": "你", "color": "#94abff"}, "：我是認真的啊！"]

scoreboard players set next_dialogue_id Dialogue.Global 15
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 41
scoreboard players set guard Dialogue.Global 1
