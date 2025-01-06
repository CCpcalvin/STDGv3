tellraw @a ["", {"text": "妹妹", "color": "#ff80f0"}, "：哥，快起床啦！"]

scoreboard players set next_dialogue_id Dialogue.Global 5
function dialogue:reset_timer
scoreboard players set time_to_next_sequence Dialogue.Global 43
scoreboard players set guard Dialogue.Global 1
