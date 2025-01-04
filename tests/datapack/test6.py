import STDGv3
import os


def main():
    sqList: list[STDGv3.Sequence] = []
    scripts_pool = "./tests/datapack/scripts"
    STDGv3.DialogueSequence.update_colormap({"嗣尤": "aqua", "幸姈": "red"})

    for file in os.listdir(scripts_pool):
        scene = file.split(".")[0]
        head = STDGv3.read_script(os.path.join(scripts_pool, file), scene)
        head.generate_dialogue_json()
        sqList.append(head)

    STDGv3.generate_datapack(
        sqList,
        "./tests/datapack/",
        "test",
        reload=True,
    )


if __name__ == "__main__":
    main()
