import STDGv3


def main():
    head = STDGv3.read_script("./tests/datapack/scripts.txt")

    print(head.next)
    print(head.get_next(1))
    print(head.get_next(5))

    print(head)
    print(head.get_pervious(1))

    last = head.get_last()
    print(last)
    print(last.pervious.get_next(3))


if __name__ == "__main__":
    main()
