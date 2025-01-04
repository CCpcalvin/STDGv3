import re


def count_chinese_characters(text):
    # Define a regular expression pattern for Chinese characters
    chinese_char_pattern = r"[\u4e00-\u9fff]"
    # chinese_char_pattern = r"\p{Han}"

    # Use re.findall to find all Chinese characters in the text
    chinese_chars = re.findall(chinese_char_pattern, text)

    # Return the count of Chinese characters
    return len(chinese_chars)


def main():
    # mystr = "嗣尤：你跟她都分手一段時間了abcdeg"
    mystr = "咱们▯国人不吃这一套！"
    chineseChar = count_chinese_characters(mystr)
    print(chineseChar)
    print(len(mystr) - chineseChar)


if __name__ == "__main__":
    main()
