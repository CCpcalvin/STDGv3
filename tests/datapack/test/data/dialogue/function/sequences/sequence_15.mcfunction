tellraw @a "你：是呀！"
scoreboard players set next_dialogue_id Dialogue.Global 16
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 20
scoreboard players set guard Dialogue.Global 1
