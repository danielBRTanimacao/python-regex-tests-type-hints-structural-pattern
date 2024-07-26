def bacon_with_eggs(n):
    assert isinstance(n, int), 'O valor "n" deve ser int'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon with eggs'
    elif n % 3 == 0:
        return 'Bacon'    
    elif n % 5 == 0:
        return 'Eggs'
    
    return 'Starve'