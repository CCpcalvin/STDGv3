tellraw @a ["", {"text": "你", "color": "#94abff"}, "：咦？怎麼跟之前不一樣，沒有女生可以選"]

scoreboard players set next_dialogue_id Dialogue.Global 1
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 93
scoreboard players set guard Dialogue.Global 1
