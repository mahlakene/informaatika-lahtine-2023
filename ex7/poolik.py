"""Poolik."""


file_to_r = "testid.windows/input_009.txt"
file_to_w = "output/output_009.txt"
with open(file_to_r, "r", encoding="windows-1252") as f:  # ISO-8859-1
    lines = f.readlines()
N = len(lines) // 2


def get_chars(word1: str, word2: str):
    """Get all chars from given two words."""
    word2_unique_chars = ""
    for i in word2:
        if i not in word1:
            word2_unique_chars += i
    return word2_unique_chars + word1


for i in range(N):
    result = ""
    consonants_only = lines[i][:-1].split(" ")
    vowels_only = lines[i + N][:-1].split(" ")
    last_char = ""
    for c, v in zip(consonants_only, vowels_only):

        if c == " " and v != " ":
            result += v + " "
        elif v == " " and c != " ":
            result += c + " "
        else:
            result += get_chars(c, v) + " "
    result += "\n"
    with open(file_to_w, "a", encoding="windows-1252") as f: # windows-1252
        f.write(result)
