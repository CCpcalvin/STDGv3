import os

import STDGv3


def main():
    sq = STDGv3.read_script("./tests/datapack/scripts/s2p2.txt", "s2p2")

    sq.get_next(11).append("function scene:2")
    sq.get_next(14).append("function scene:2")

    sqnext = sq.search_cmd_next("function scene:")
    print(sqnext)
    print(sqnext.search_cmd_next("function scene:"))

    sqnext = sq.search_dialogue_next("別玩呀，我")
    print(sqnext)


if __name__ == "__main__":
    main()
