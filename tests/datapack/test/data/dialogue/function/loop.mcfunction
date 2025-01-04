execute if score timer Dialogue.Global >= time_to_next_sequence Dialogue.Global run function dialogue:run_scene
scoreboard players add timer Dialogue.Global 1
scoreboard players set guard Dialogue.Global 0
