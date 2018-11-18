from mathematica.geometry.figures import square_area, triangle_area

#from mathemaica.geometry import figures

def test_square_area():
    assert square_area(2) == 4
    assert square_area(-10) == None
def test_triangle_area():
    assert triangle_area(4, 4) == 8
    assert triangle_area(1, 2) == 1