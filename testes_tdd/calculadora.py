def soma(x: int | float, y: int | float) -> float:
    """
        Soma x e y
    >>> soma('10', 20)
    30
    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    return x + y
    # utilizando assertions (principalmente usado para devs não para user final)
    # utilizando DocTest

if __name__ == "__main__":
    import doctest

    doctest.testmod()