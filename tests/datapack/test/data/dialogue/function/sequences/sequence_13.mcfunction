tellraw @a "你：我是認真的啊！"
scoreboard players set next_dialogue_id Dialogue.Global 14
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 41
scoreboard players set guard Dialogue.Global 1
