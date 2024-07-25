def soma(x: int | float, y: int | float) -> float:
    """
        Soma x e y
    >>> soma('10', 20)
    30

    >>> soma(10, -10)
    0

    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    return x + y
    # utilizando assertions (principalmente usado para devs não para user final)
    # utilizando DocTest

def subtra(x, y):
    # Função que faz apenas uma coisa
    """
    >>> subtra(10, 10)
    0
    """
    return x - y

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)