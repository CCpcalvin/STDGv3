tellraw @a "你：她身處另一個平行宇宙，努力找出與我相遇的方法"
scoreboard players set next_dialogue_id Dialogue.Global 10
function dialogue:helper/reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 20