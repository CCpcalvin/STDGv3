tellraw @a "嗣尤：你真誠地相信，將來會跟平行宇宙的女生在一起？"
scoreboard players set next_dialogue_id Dialogue.Global 15
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 20
scoreboard players set guard Dialogue.Global 1
