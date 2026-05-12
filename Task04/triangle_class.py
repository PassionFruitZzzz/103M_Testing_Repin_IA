from typing import Union, Tuple

class IncorrectTriangleSides(Exception):
    """Исключение для неверных длин сторон треугольника."""
    pass

class Triangle:
    def __init__(self, a: Union[int, float], b: Union[int, float], c: Union[int, float]):
        # Проверка типов
        if not all(isinstance(x, (int, float)) for x in (a, b, c)):
            raise IncorrectTriangleSides("Все стороны должны быть числами")
        
        sides = sorted([a, b, c])
        # Проверка положительности и неравенства треугольника
        if sides[0] <= 0 or sides[0] + sides[1] <= sides[2]:
            raise IncorrectTriangleSides("Стороны не образуют треугольник")
        
        self._sides = (float(a), float(b), float(c))  # храним как float для единообразия
    
    def perimeter(self) -> float:
        """Возвращает периметр треугольника."""
        return sum(self._sides)
    
    def triangle_type(self) -> str:
        """
        Возвращает тип треугольника:
        - "equilateral" – равносторонний,
        - "isosceles" – равнобедренный,
        - "nonequilateral" – разносторонний.
        """
        a, b, c = self._sides
        if a == b == c:
            return "equilateral"
        if a == b or b == c or a == c:
            return "isosceles"
        return "nonequilateral"