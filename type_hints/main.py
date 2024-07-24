# uma_string: str = 'Uma string'
# um_inteiro: int = 123456789
# um_float: float = 1.234
# um_boolean: bool = True
# um_set: set = {1, 2, 3} # mais sobre a seguir
# uma_lista: list = [] # mais a seguir
# uma_tupla: tuple = 1, 2, 3 # mais a seguir
# um_dicionario: dict = {} # mais sobre a seguir

# def soma(x: int, y: int, z: float) -> float:
#     return x + y + z

# print(soma(10, 10, 5.3))

# lista_inteiros: list[int] = [1, 2, 3, 4, 5, 6]
# lista_string: list[str] = ['a', 'b', 'c']
# lista_tuple: list[tuple] = [(1, 2), (3, '4'), ('5', 6)]
# lista_lista_lista: list[list[int]] = [[1], [2], [3]]

# lista_dict: list[dict[str, int]] = [
#     {
#         'value': 1,
#         'value1': 2,
#     },
#     {
#         'value': 1,
#         'value1': 2,
#     },
# ]

# lista_dict_list: dict[str, list[int]] = {
#     'value1': [1, 2, 3],
#     'value2': [4, 5, 6],
# }

# set_int: set[int] = {1, 2, 3}

# listaDeInteiros = list[int] # type alias
# dictListaDeInteiros = dict[str, listaDeInteiros]

# dicionario_lista_de_inteiros: dictListaDeInteiros = {
#     'a': [1, 2, 3]
# }

# string_e_inteiro: str | int = 1 # Union

# def som(x: int, y: float | None = None) -> float:
#     return x + y

# def soma(x: int, y: float | None = None) -> float:
#     if isinstance(y, float | int): return x + y
#     return x + x

# print(soma(1, 2.2))

# from collections.abc import Callable    

# SomInteiros = Callable[[int, int], int]

# def execute(func: SomInteiros, a: int, b: int) -> int:
#     return func(a, b)

# def soma(a: int, b:int) -> int:
#     return a + b

# print(execute(soma, 10, 10))

# from typing import TypeVar

# T = TypeVar('T') # um tipo dinamico

# def get_item(list_: list[T], index: int) -> T:
#     return list_[index]

# list_int = get_item([1, 2, 3], 1)
# list_int = get_item(['a', 'b', 'c'], 1)

class Person:
    def __init__(self, firstname, lastname) -> None:
        self.first_name = firstname
        self.last_name = lastname

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    

def say_my_name(person: Person) -> str:
    return person.full_name

print(say_my_name(Person('Bico', 'Seco')))