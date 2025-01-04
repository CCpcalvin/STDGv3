import STDGv3


def main():
    head = STDGv3.read_script("./tests/datapack/scripts/s2p2.txt", "s2p2")
    head.print_tree()
    head.generate_entire_sequence("./tests/datapack/", "test", reload=True)


if __name__ == "__main__":
    main()
