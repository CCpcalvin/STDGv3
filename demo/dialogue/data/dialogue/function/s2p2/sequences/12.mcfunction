tellraw @a ["", {"text": "嗣尤", "color": "aqua"}, "：別玩呀，我是認真問的啊！"]

scoreboard players set next_dialogue_id Dialogue.Global 13
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 68
scoreboard players set guard Dialogue.Global 1
