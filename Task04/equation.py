import math
from typing import List, Optional, Union

def find_roots(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> Optional[List[float]]:
    """
    Вычисляет корни квадратного уравнения ax^2 + bx + c = 0.
    
    Возвращает:
    - список из одного или двух корней, отсортированных по возрастанию,
    - пустой список, если действительных корней нет,
    - None, если уравнение тождественно верно (0 = 0).
    
    Примеры:
    >>> find_roots(1, -3, 2)
    [1.0, 2.0]
    >>> find_roots(1, 2, 1)
    [-1.0]
    >>> find_roots(1, 0, 1)
    []
    >>> find_roots(0, 2, -4)
    [2.0]
    >>> find_roots(0, 0, 5)
    []
    >>> find_roots(0, 0, 0) is None
    True
    """
    # Линейное уравнение
    if a == 0:
        if b == 0:
            # Вырожденные случаи
            return None if c == 0 else []
        # bx + c = 0 -> x = -c/b
        return [round(-c / b, 10)]
    
    # Квадратное уравнение
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return []
    
    if discriminant == 0:
        root = -b / (2 * a)
        return [round(root, 10)]
    
    sqrt_d = math.sqrt(discriminant)
    x1 = (-b - sqrt_d) / (2 * a)
    x2 = (-b + sqrt_d) / (2 * a)
    roots = sorted([round(x1, 10), round(x2, 10)])
    return roots

if __name__ == "__main__":
    import doctest
    doctest.testmod()