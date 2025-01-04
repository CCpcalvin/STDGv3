tellraw @a ["你：如果你某天玩了一張地圖"]

scoreboard players set next_dialogue_id Dialogue.Global 11
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 63
scoreboard players set guard Dialogue.Global 1
