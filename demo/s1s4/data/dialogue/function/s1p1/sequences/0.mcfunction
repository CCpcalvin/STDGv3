tellraw @a ["???：我想我們不是那麼適合"]

scoreboard players set next_dialogue_id Dialogue.Global 1
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 61
scoreboard players set guard Dialogue.Global 1
