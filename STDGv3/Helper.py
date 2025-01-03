import os, json
from shutil import rmtree



def gen_mcmeta(pack_format: int, description: str) -> str:
    MCMETA = {"pack": {"pack_format": pack_format, "description": description}}
    return json.dumps(MCMETA, ensure_ascii=False)


def create_datapack(
    datapack_path: str,
    datapack_name: str,
    pack_format: int = 61,
    datapack_description: str = "STDGv3",
) -> str:
    cursor = os.path.join(datapack_path, datapack_name)

    # Delete the datapack if it exists
    if datapack_name in os.listdir(datapack_path):
        rmtree(cursor)

    # Create new directory
    os.mkdir(cursor)

    os.mkdir(os.path.join(cursor, "data"))

    # Create .mcmeta file
    with open(os.path.join(cursor, "pack.mcmeta"), "w", encoding="utf-8") as f:
        f.write(gen_mcmeta(pack_format, datapack_description))

    return os.path.join(cursor, "data")
