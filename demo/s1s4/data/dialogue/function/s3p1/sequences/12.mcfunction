tellraw @a ["", {"text": "你", "color": "#94abff"}, "：總之那地圖害我玩太久，沒空理會女朋友！"]

scoreboard players set next_dialogue_id Dialogue.Global 13
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 98
scoreboard players set guard Dialogue.Global 1
