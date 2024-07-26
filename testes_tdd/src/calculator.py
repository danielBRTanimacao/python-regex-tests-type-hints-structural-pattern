def sum_(x: float | int, y: float | int) -> float:
    assert isinstance(x, (float, int)), 'Valor X deve ser inteiro ou ponto flutuante'
    return x + y

def mult_(x: float | int, y: float | int) -> float:
    return x * y