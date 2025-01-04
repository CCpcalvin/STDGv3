import copy

import STDGv3


def main():
    head = STDGv3.read_script("./tests/datapack/scripts_short.txt")
    head.print_tree()

    last = head.get_last()
    head = last.get_head()
    head.print_tree()

    tpSq = STDGv3.Sequence(
        ["function scene:start", "function scene:1", "function scene:2"]
    )
    head.insert_after(copy.deepcopy(tpSq))
    head.insert_before(copy.deepcopy(tpSq))

    head = head.get_head()
    head.print_tree()

    last = head.get_last()
    last.insert_before(copy.deepcopy(tpSq))
    last.insert_after(copy.deepcopy(tpSq))

    head.generate_dialogue_json()
    head.print_tree()
    head.generate_datapack("./tests/datapack/", "test", reload=True)


if __name__ == "__main__":
    main()
