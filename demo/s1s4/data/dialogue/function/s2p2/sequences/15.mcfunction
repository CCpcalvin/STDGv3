tellraw @a ["", {"text": "嗣尤", "color": "#ffb974"}, "：", {"text": "你", "color": "#94abff"}, "真誠地相信，將來會跟平行宇宙的女生在一起？"]

scoreboard players set next_dialogue_id Dialogue.Global 16
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 118
scoreboard players set guard Dialogue.Global 1
