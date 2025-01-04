import STDGv3


def main():
    head = STDGv3.read_script("./tests/datapack/scripts.txt")
    head.print_tree()
    head.generate_datapack("./tests/datapack/", "test", reload=True)


if __name__ == "__main__":
    main()
