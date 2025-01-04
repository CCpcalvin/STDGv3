tellraw @a "嗣尤：別玩呀，我是認真問的啊！"
scoreboard players set next_dialogue_id Dialogue.Global 13
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 20
scoreboard players set guard Dialogue.Global 1
