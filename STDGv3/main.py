from .Sequence import Sequence
from .DialogueSequence import DialogueSequence

from .gen import *

import os


def read_script(path: str, scene: str):
    """
    Reads a script file and constructs a linked list of DialogueSequence objects.

    Args:
        path (str): The path to the script file to be read.
        scene (str): The scene identifier for the DialogueSequence objects.

    Returns:
        DialogueSequence: The head of the linked list of DialogueSequence objects.
    """

    with open(path, "r", encoding="utf-8") as f:
        head = DialogueSequence(scene, next(f))
        last = head

        for i, line in enumerate(f):
            this = DialogueSequence(scene, line)
            last.next = this
            this.pervious = last

            last = this

    return head


def generate_datapack(
    sequence_list: list[Sequence],
    datapack_path: str,
    datapack_name: str,
    pack_format: int = 61,
    datapack_description: str = "STDGv3",
    reload: bool = False,
):
    """
    Generate a datapack given a list of sequences.

    Args:
        sequence_list (list[Sequence]): The list of sequences to be generated.
        datapack_path (str): The path where the datapack is located.
        datapack_name (str): The name of the datapack.
        pack_format (int, optional): The pack format of the datapack. Defaults to 61.
        datapack_description (str, optional): The description of the datapack. Defaults to "STDGv3".
        reload (bool, optional): Whether to reload the datapack if it already exists. Defaults to False.
    """

    data_path = create_datapack(
        datapack_path, datapack_name, pack_format, datapack_description, reload
    )

    run_scene_file = open(
        os.path.join(data_path, FUNCTION_PATH, f"{RUN_SCENE_FUNCTION}.mcfunction"),
        "w",
        encoding="utf-8",
    )

    for i, seq in enumerate(sequence_list):
        seq.generate_entire_sequence(i, data_path)
        run_scene_file.write(
            f"execute if score {SCENE_ID} {GLOBAL_SCOREBOARD_OBJ} matches {i} run "
            + seq.get_run_sequence_cmd()
        )

    run_scene_file.close()

    init_datapack(data_path)
