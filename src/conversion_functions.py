from typing import Tuple

def tuple_to_str(t: Tuple[int]) -> str:
    return '-'.join(str(nombre) for nombre in t)


def str_to_tuple(s: str) ->  Tuple[int]:
    sous_chaines = s.split('-')
    return tuple(int(s) for s in sous_chaines)


if __name__ == '__main__':
    print(tuple_to_str((3, 7, 12, 5, 9)))
    print(str_to_tuple(("3-7-12-5-9")))