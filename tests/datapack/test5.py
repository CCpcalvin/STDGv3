import STDGv3


def main():
    head = STDGv3.read_script("./tests/datapack/scripts_short.txt")
    head.generate_dialogue_cmd()
    head.append("function scene:start")

    next = head.get_next(1)
    next.extend(["function scene:1", "function scene:2"])

    head.print_tree()
    head.generate_datapack("./tests/datapack/", "test", reload=True)


if __name__ == "__main__":
    main()
