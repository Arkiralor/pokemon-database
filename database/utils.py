from ast import literal_eval


def rip_string_proto(abl: str):
    banned_characters = {"[", "'", ",", "]"}
    list_of_char = []
    inv = 0
    list_of_char[:0] = abl
    for i in range(len(list_of_char)-1):
        if list_of_char[i] in banned_characters:
            list_of_char[i] = inv
        else:
            pass

    while inv in list_of_char:
        list_of_char.remove(inv)

    del list_of_char[len(list_of_char)-1]

    return ''.join(list_of_char).split(" ")


def rip_string(orig: str):
    return literal_eval(orig)
