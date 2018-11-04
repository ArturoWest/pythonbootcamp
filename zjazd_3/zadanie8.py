class Vector:
    def __init__(self, x, y,):
        self.x = x
        self.y = y

    def __add__(self, other):
       return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.length() < other.length()

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y )


    def length(selfself):
        return ((self.x **2 + self.y **2)**0,5

def test_vector_add():
    v_1 = Vector(1, 3)
    v_2 = Vector(4, 7)

    result = v_1 + v_2

    assert result.x == 5
    assert result.y == 10
   #assert v_1 + v_2 =  Vector(1,3)

def test_vector_sub():
    v_1 = Vector(1, 3)
    v_2 = Vector(4, 7)

    result = v_1 - v_2

    assert result.x == -3
    assert result.y == -4

def test_vector_equal():
    v_1 = Vector(1, 3)
    v_2 = Vector(1, 7)
    v_3 = Vector(4, 7)

    assert v_1 == v_2
    assert not (v_1 == v_3)

def test_vector_length():
    vector = Vector(2, 2)
    assert vector.length()) == (2 ** 2 + 2 ** 2) ** 0,5

def test_vector_lower_than():
    v1 = Vector (1, 3)
    v2 == Vector(1, 2)
    assert not (v1 < v2)
    assert v2 < v1

def test_vector_multiplicatrion_with_scalar():
    vector = Vector(2, 4)
    result = vector *2
    assert result.x == 4
    assert result.y == 8
