import json
import os
from shutil import rmtree

# Parameters
NAMESPACE: str = "dialogue"
FUNCTION_TAG_PATH: str = os.path.join("minecraft", "tags", "function")
LOAD_TAG_PATH: str = os.path.join(FUNCTION_TAG_PATH, "load.json")
TICK_TAG_PATH: str = os.path.join(FUNCTION_TAG_PATH, "tick.json")

FUNCTION_PATH: str = os.path.join(NAMESPACE, "function")

LOAD_FUNCTION = "load"
LOAD_FUNCTION_PATH: str = os.path.join(FUNCTION_PATH, f"{LOAD_FUNCTION}.mcfunction")

TICK_FUNCTION = "tick"
TICK_FUNCTION_PATH: str = os.path.join(FUNCTION_PATH, f"{TICK_FUNCTION}.mcfunction")

LOOP_FUNCTION = "loop"
LOOP_FUNCTION_PATH: str = os.path.join(FUNCTION_PATH, f"{LOOP_FUNCTION}.mcfunction")

RUN_SEQUENCES_FUNCTION = "run_sequences"
RUN_SEQUENCES_CMD = f"function {NAMESPACE}:{RUN_SEQUENCES_FUNCTION}\n"

RUN_SCENE_FUNCTION = "run_scene"
RUN_SCENE_CMD = f"function {NAMESPACE}:{RUN_SCENE_FUNCTION}\n"

UNINSTALL_FUNCTIONPATH: str = os.path.join(FUNCTION_PATH, "uninstall.mcfunction")

SEQUENCES_SUBPATH = "sequences"
START_ID = 0
TICK_PER_SECOND = 20
DEFAULT_SEQUENCES_INTERVAL = 20

# Scoreboard constants
GLOBAL_SCOREBOARD_OBJ: str = "Dialogue.Global"
TIMER: str = "timer"
NEXT_DIALOGUE_ID: str = "next_dialogue_id"
PAUSE: str = "pause"
TIME_TO_NEXT_SEQUENCE: str = "time_to_next_sequence"
SEQUENCE_GUARD: str = "guard"
SCENE_ID: str = "scene_id"

# Commands
RESET_TIMER_CMD = f"function {NAMESPACE}:helper/reset_timer\n"
FORCE_RESET_CMD = f"function {NAMESPACE}:helper/force_reset\n"
TIMER_LOOP_CMD = f"scoreboard players add {TIMER} {GLOBAL_SCOREBOARD_OBJ} 1\n"
SET_GUARD_CMD = f"scoreboard players set {SEQUENCE_GUARD} Dialogue.Global 1\n"
REMOVE_GUARD_CMD = f"scoreboard players set {SEQUENCE_GUARD} Dialogue.Global 0\n"


def gen_mcmeta(pack_format: int, description: str) -> str:
    MCMETA = {"pack": {"pack_format": pack_format, "description": description}}
    return json.dumps(MCMETA, ensure_ascii=False)


def set_next_dialogue_id(id: int):
    return f"scoreboard players set {NEXT_DIALOGUE_ID} Dialogue.Global {id}\n"


def set_time_to_next_sequence(time: int):
    return f"scoreboard players set {TIME_TO_NEXT_SEQUENCE} Dialogue.Global {time}\n"


def set_pause():
    return f"scoreboard players set {PAUSE} Dialogue.Global 1\n"


def stop_pause():
    return f"scoreboard players set {PAUSE} Dialogue.Global 0\n"


def run_sequence(id: int):
    return f"function {NAMESPACE}:sequences/sequence_{id}\n"


def create_datapack(
    datapack_path: str,
    datapack_name: str,
    pack_format: int = 61,
    datapack_description: str = "STDGv3",
    reload: bool = False,
) -> str:
    cursor = os.path.join(datapack_path, datapack_name)

    # Delete the datapack if it exists
    if datapack_name in os.listdir(datapack_path):
        if reload:
            rmtree(cursor)

        else:
            raise Exception("Datapack already exists")

    # Create new directory
    os.mkdir(cursor)

    data_path = os.path.join(cursor, "data")
    os.mkdir(data_path)

    # Create .mcmeta file
    with open(os.path.join(cursor, "pack.mcmeta"), "w", encoding="utf-8") as f:
        f.write(gen_mcmeta(pack_format, datapack_description))

    # Create tags directory
    os.makedirs(os.path.join(data_path, "minecraft", "tags", "function"))

    # Create functions directory
    os.makedirs(os.path.join(data_path, FUNCTION_PATH))

    return data_path


def get_show_display_function(data_path: str):
    # Show display functions
    display_cmd_str = (
        f"scoreboard objectives setdisplay sidebar {GLOBAL_SCOREBOARD_OBJ} \n"
    )

    with open(
        os.path.join(data_path, FUNCTION_PATH, "debug/show_display.mcfunction"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(display_cmd_str)


def set_scene_id(id: int):
    return f"scoreboard players set {SCENE_ID} Dialogue.Global {id}\n"


def get_force_reset_function(data_path: str):
    # Get force reset functions
    force_reset_cmd_str = RESET_TIMER_CMD
    force_reset_cmd_str += set_next_dialogue_id(9999)
    force_reset_cmd_str += set_pause()
    force_reset_cmd_str += set_time_to_next_sequence(9999)
    force_reset_cmd_str += SET_GUARD_CMD
    force_reset_cmd_str += set_scene_id(9999)

    with open(
        os.path.join(data_path, FUNCTION_PATH, "helper/force_reset.mcfunction"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(force_reset_cmd_str)


def get_reset_timer_function(data_path: str):
    reset_timer_cmd_str = f"scoreboard players set {TIMER} {GLOBAL_SCOREBOARD_OBJ} 0\n"
    with open(
        os.path.join(data_path, FUNCTION_PATH, "helper/reset_timer.mcfunction"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(reset_timer_cmd_str)


def get_pause_function(data_path: str):
    pause_cmd_str = set_pause()
    with open(
        os.path.join(data_path, FUNCTION_PATH, "helper/pause.mcfunction"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(pause_cmd_str)


def get_stop_pause_function(data_path: str):
    stop_pause_cmd_str = stop_pause()
    with open(
        os.path.join(data_path, FUNCTION_PATH, "helper/stop_pause.mcfunction"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(stop_pause_cmd_str)


def get_stop_function(data_path: str):
    stop_cmd_str = set_pause()
    stop_cmd_str += FORCE_RESET_CMD
    with open(
        os.path.join(data_path, FUNCTION_PATH, "helper/stop.mcfunction"),
        "w",
        encoding="utf-8",
    ) as f:
        f.write(stop_cmd_str)


def init_datapack(data_path: str):
    # Get debug functions
    os.makedirs(os.path.join(data_path, FUNCTION_PATH, "debug"))
    get_show_display_function(data_path)

    # Get helper function
    os.makedirs(os.path.join(data_path, FUNCTION_PATH, "helper"))
    get_force_reset_function(data_path)
    get_reset_timer_function(data_path)
    get_pause_function(data_path)
    get_stop_pause_function(data_path)
    get_stop_function(data_path)

    # Get the init function
    load_cmd_str = f"scoreboard objectives add {GLOBAL_SCOREBOARD_OBJ} dummy\n"
    load_cmd_str += FORCE_RESET_CMD
    with open(os.path.join(data_path, LOAD_FUNCTION_PATH), "w", encoding="utf-8") as f:
        f.write(load_cmd_str)

    # Link the init function to init tag
    load_json = {"values": [f"{NAMESPACE}:{LOAD_FUNCTION}"]}
    with open(os.path.join(data_path, LOAD_TAG_PATH), "w", encoding="utf-8") as f:
        json.dump(load_json, f)

    # Get the uninstall function
    uninstall_cmd_str = f"scoreboard objectives remove {GLOBAL_SCOREBOARD_OBJ}\n"
    with open(
        os.path.join(data_path, UNINSTALL_FUNCTIONPATH), "w", encoding="utf-8"
    ) as f:
        f.write(uninstall_cmd_str)

    # Get the tick function
    tick_cmd_str = f"execute if score {PAUSE} {GLOBAL_SCOREBOARD_OBJ} matches 0 run function {NAMESPACE}:{LOOP_FUNCTION}\n"
    with open(os.path.join(data_path, TICK_FUNCTION_PATH), "w", encoding="utf-8") as f:
        f.write(tick_cmd_str)

    # Link the tick function to tick tag
    tick_json = {"values": [f"{NAMESPACE}:{TICK_FUNCTION}"]}
    with open(os.path.join(data_path, TICK_TAG_PATH), "w", encoding="utf-8") as f:
        json.dump(tick_json, f)

    # Get the loop function
    loop_cmd_str = (
        f"execute if score {TIMER} {GLOBAL_SCOREBOARD_OBJ} >= {TIME_TO_NEXT_SEQUENCE} {GLOBAL_SCOREBOARD_OBJ} run "
        + RUN_SCENE_CMD
    )
    loop_cmd_str += TIMER_LOOP_CMD
    loop_cmd_str += REMOVE_GUARD_CMD
    with open(os.path.join(data_path, LOOP_FUNCTION_PATH), "w") as f:
        f.write(loop_cmd_str)
