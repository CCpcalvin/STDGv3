tellraw @a ["", {"text": "你", "color": "#94abff"}, "：她身處另一個平行宇宙，努力找出與我相遇的方法"]

scoreboard players set next_dialogue_id Dialogue.Global 10
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 116
scoreboard players set guard Dialogue.Global 1
