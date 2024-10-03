# 1. rotateR for strings
def rotate_r(string: str) -> str:
    return string[-1] + string[:-1]


# 2. rotateL for lists
def rotate_l(sequence: list) -> list:
    return sequence[1:] + [sequence[0]]


# 3. make it work for strings and lists
def rotate_l_generic(iterable):
    return iterable[1:] + ([iterable[0]] if isinstance(iterable, list) else iterable[0])


# 4. rotateRx in-place
def rotate_r_in_place(sequence: list) -> None:
    sequence[:] = sequence[-1:] + sequence[:-1]


# 5. rotateRx for strings
# does not work, string is immutable


# 6. rotateR2 using only rotate_r
def rotate_r_2(string: str) -> str:
    return rotate_r(rotate_r(string))


# 7. rotateRx2 using only rotate_r_in_place
def rotate_r_in_place_2(sequence: list) -> None:
    rotate_r_in_place(sequence)
    rotate_r_in_place(sequence)


# 8. list that rotates both inner lists
inner = [1, 2, 3]
outer = [inner, inner]
