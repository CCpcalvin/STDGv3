tellraw @a ["", {"text": "你", "color": "#94abff"}, "：但我相信，有朝一日，一個跟我相愛的女生會出現"]

scoreboard players set next_dialogue_id Dialogue.Global 7
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 113
scoreboard players set guard Dialogue.Global 1
