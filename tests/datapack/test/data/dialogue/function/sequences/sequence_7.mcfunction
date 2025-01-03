tellraw @a "你：可是現在我們被無數世界相隔"
scoreboard players set next_dialogue_id Dialogue.Global 8
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 20
