tellraw @a "嗣尤：你跟她都分手一段時間了
"
scoreboard players set next_dialogue_id Dialogue.Global 1
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 20
