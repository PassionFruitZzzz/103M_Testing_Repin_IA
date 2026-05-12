import pytest
from triangle_class import Triangle, IncorrectTriangleSides

# ---------- Позитивные тесты ----------
@pytest.mark.parametrize("a,b,c,expected_type", [
    (5, 5, 5, "equilateral"),
    (3, 3, 5, "isosceles"),
    (4, 5, 4, "isosceles"),
    (6, 9, 5, "nonequilateral"),
    (2.5, 2.5, 3.0, "isosceles"),
])
def test_triangle_type_positive(a, b, c, expected_type):
    t = Triangle(a, b, c)
    assert t.triangle_type() == expected_type

@pytest.mark.parametrize("a,b,c,expected_perimeter", [
    (5, 5, 5, 15),
    (3, 4, 5, 12),
    (2.5, 2.5, 4.0, 9.0),
])
def test_perimeter(a, b, c, expected_perimeter):
    t = Triangle(a, b, c)
    assert t.perimeter() == expected_perimeter

# ---------- Негативные тесты (некорректные стороны) ----------
@pytest.mark.parametrize("a,b,c", [
    (0, 4, 5),    # нулевая сторона
    (-1, 2, 2),   # отрицательная
    (1, 2, 10),   # неравенство треугольника
    (2, 2, 4),    # вырожденный
    ("3", 4, 5),  # строка
    (3, "4", 5),  # строка на втором месте
    (None, 4, 5), # None
])
def test_incorrect_sides_raise_exception(a, b, c):
    with pytest.raises(IncorrectTriangleSides):
        Triangle(a, b, c)

# Тест на корректность хранения сторон как float
def test_stores_floats():
    t = Triangle(3, 4, 5)
    assert all(isinstance(s, float) for s in t._sides)