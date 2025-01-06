tellraw @a ["", {"text": "幸姈", "color": "#ffbac6"}, "：", {"text": "你", "color": "#94abff"}, "好，我是", {"text": "幸姈", "color": "#ffbac6"}, "，我們終於見面了"]

scoreboard players set next_dialogue_id Dialogue.Global 10
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 83
scoreboard players set guard Dialogue.Global 1
