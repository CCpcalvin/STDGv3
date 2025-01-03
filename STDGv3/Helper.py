import os, json
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
RUN_SEQUENCES_FUNCTION_PATH: str = os.path.join(
    FUNCTION_PATH, f"{RUN_SEQUENCES_FUNCTION}.mcfunction"
)

UNINSTALL_FUNCTIONPATH: str = os.path.join(FUNCTION_PATH, "uninstall.mcfunction")

SEQUENCES_PATH = os.path.join(FUNCTION_PATH, "sequences")
DEFAULT_SEQUENCES_INTERVAL = 20

# Scoreboard constants
GLOBAL_SCOREBOARD_OBJ: str = "Dialogue.Global"
TIMER: str = "timer"
NEXT_DIALOGUE_ID: str = "next_dialogue_id"
PAUSE: str = "pause"
TIME_TO_NEXT_SEQUENCE: str = "time_to_next_sequence"

# Commands
RESET_TIMER_CMD = f"function {NAMESPACE}:helper/reset_timer\n"
TIMER_LOOP_CMD = f"scoreboard players add {TIMER} {GLOBAL_SCOREBOARD_OBJ} 1\n"


def gen_mcmeta(pack_format: int, description: str) -> str:
    MCMETA = {"pack": {"pack_format": pack_format, "description": description}}
    return json.dumps(MCMETA, ensure_ascii=False)


def set_next_dialogue_id(id: int):
    return f"scoreboard players set {NEXT_DIALOGUE_ID} Dialogue.Global {id}\n"


def set_time_to_next_sequence(time: int):
    return f"scoreboard players set {TIME_TO_NEXT_SEQUENCE} Dialogue.Global {time}\n"


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
        os.path.join(data_path, FUNCTION_PATH, "debug/show_display.mcfunction"), "w"
    ) as f:
        f.write(display_cmd_str)


def get_force_reset_function(data_path: str):
    # Get force reset functions
    force_reset_cmd_str = RESET_TIMER_CMD
    force_reset_cmd_str += (
        f"scoreboard players set {NEXT_DIALOGUE_ID} {GLOBAL_SCOREBOARD_OBJ} 0\n"
    )
    force_reset_cmd_str += f"scoreboard players set {PAUSE} {GLOBAL_SCOREBOARD_OBJ} 1\n"
    force_reset_cmd_str += (
        f"scoreboard players set {TIME_TO_NEXT_SEQUENCE} {GLOBAL_SCOREBOARD_OBJ} 9999\n"
    )

    with open(
        os.path.join(data_path, FUNCTION_PATH, "helper/force_reset.mcfunction"), "w"
    ) as f:
        f.write(force_reset_cmd_str)


def get_reset_timer_function(data_path: str):
    reset_timer_cmd_str = f"scoreboard players set {TIMER} {GLOBAL_SCOREBOARD_OBJ} 0\n"
    with open(
        os.path.join(data_path, FUNCTION_PATH, "helper/reset_timer.mcfunction"), "w"
    ) as f:
        f.write(reset_timer_cmd_str)


def init_datapack(data_path: str):
    # Get debug functions
    os.makedirs(os.path.join(data_path, FUNCTION_PATH, "debug"))
    get_show_display_function(data_path)

    # Get helper function
    os.makedirs(os.path.join(data_path, FUNCTION_PATH, "helper"))
    get_force_reset_function(data_path)
    get_reset_timer_function(data_path)

    # Get the init function
    load_cmd_str = f"scoreboard objectives add {GLOBAL_SCOREBOARD_OBJ} dummy\n"
    load_cmd_str += f"function {NAMESPACE}:debug/force_reset\n"
    with open(os.path.join(data_path, LOAD_FUNCTION_PATH), "w") as f:
        f.write(load_cmd_str)

    # Link the init function to init tag
    load_json = {"values": [f"{NAMESPACE}:{LOAD_FUNCTION}"]}
    with open(os.path.join(data_path, LOAD_TAG_PATH), "w") as f:
        json.dump(load_json, f)

    # Get the uninstall function
    uninstall_cmd_str = f"scoreboard objectives remove {GLOBAL_SCOREBOARD_OBJ}\n"
    with open(os.path.join(data_path, UNINSTALL_FUNCTIONPATH), "w") as f:
        f.write(uninstall_cmd_str)

    # Get the tick function
    tick_cmd_str = f"execute if score {PAUSE} {GLOBAL_SCOREBOARD_OBJ} matches 0 run function {NAMESPACE}:{LOOP_FUNCTION}\n"
    with open(os.path.join(data_path, TICK_FUNCTION_PATH), "w") as f:
        f.write(tick_cmd_str)

    # Link the tick function to tick tag
    tick_json = {"values": [f"{NAMESPACE}:{TICK_FUNCTION}"]}
    with open(os.path.join(data_path, TICK_TAG_PATH), "w") as f:
        json.dump(tick_json, f)

    # Get the loop function
    loop_cmd_str = f"execute if score {TIMER} {GLOBAL_SCOREBOARD_OBJ} = {TIME_TO_NEXT_SEQUENCE} {GLOBAL_SCOREBOARD_OBJ} run function {NAMESPACE}:{RUN_SEQUENCES_FUNCTION}\n"
    loop_cmd_str += TIMER_LOOP_CMD
    with open(os.path.join(data_path, LOOP_FUNCTION_PATH), "w") as f:
        f.write(loop_cmd_str)

