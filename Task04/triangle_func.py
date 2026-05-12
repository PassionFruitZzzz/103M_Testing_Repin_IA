from typing import Literal, Union

class IncorrectTriangleSides(Exception):
    """Исключение для неверных длин сторон."""
    pass

def get_triangle_type(side_a: Union[int, float], side_b: Union[int, float], side_c: Union[int, float]) -> Literal["equilateral", "isosceles", "nonequilateral"]:
    """
    Определяет тип треугольника по трём сторонам.
    
    Возвращает:
    - "equilateral" – равносторонний,
    - "isosceles" – равнобедренный,
    - "nonequilateral" – разносторонний.
    
    Если стороны не удовлетворяют условию существования треугольника (каждая сторона > 0
    и сумма двух любых сторон больше третьей), выбрасывается IncorrectTriangleSides.
    
    Примеры:
    >>> get_triangle_type(7, 7, 7)
    'equilateral'
    >>> get_triangle_type(8, 8, 5)
    'isosceles'
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(0, 5, 5)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Стороны должны быть положительными числами
    >>> get_triangle_type(1, 1, 3)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Нарушено неравенство треугольника
    >>> get_triangle_type('a', 5, 5)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Стороны должны быть числами
    """
    # Проверка типа
    for side in (side_a, side_b, side_c):
        if not isinstance(side, (int, float)):
            raise IncorrectTriangleSides("Стороны должны быть числами")
    
    # Проверка положительности
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        raise IncorrectTriangleSides("Стороны должны быть положительными числами")
    
    # Проверка неравенства треугольника
    a, b, c = sorted([side_a, side_b, side_c])
    if a + b <= c:
        raise IncorrectTriangleSides("Нарушено неравенство треугольника")
    
    # Определение типа
    if side_a == side_b == side_c:
        return "equilateral"
    if side_a == side_b or side_b == side_c or side_a == side_c:
        return "isosceles"
    return "nonequilateral"

if __name__ == "__main__":
    import doctest
    doctest.testmod()