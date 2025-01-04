tellraw @a ["你：不過你懂啦，我也想拍拖【談戀愛】嘛~"]

scoreboard players set next_dialogue_id Dialogue.Global 15
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 88
scoreboard players set guard Dialogue.Global 1
