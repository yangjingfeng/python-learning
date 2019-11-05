def non_repeat(line):
    """Input: string.

    Function finds the first longest substring with all unique letters.

    Output: string.
    """
    char_idx_dict = {}
    len_substring = len_best = cur_pos = tail = 0

    for index, char in enumerate(line):
        idx_char = char_idx_dict.get(char, -1)
        char_idx_dict[char] = index
        if idx_char < cur_pos:
            len_substring += 1
        else:
            if len_substring > len_best:
                tail = cur_pos
                len_best = len_substring
            len_substring -= idx_char - cur_pos
            cur_pos = idx_char + 1

    if len_substring > len_best:
        tail = cur_pos
        len_best = len_substring

    return line[tail: tail + len_best]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')