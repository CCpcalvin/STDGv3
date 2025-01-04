from .Sequence import Sequence
from .DialogueSequence import DialogueSequence

from .gen import *

import os


def read_script(path: str, scene: str):
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
