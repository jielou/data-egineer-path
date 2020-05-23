class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(f"rectangle area is {area}")
        return area

    def perimeter(self):
        peri = 2 * self.length + 2 * self.width
        print(f"rectangle perimeter is {peri}")
        return peri

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        # equivalent: super(Square, self).__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        area = 0.5 * self.base * self.height
        print(f"triangle area is : {area}")
        return area

    def perimeter(self):
        peri = self.base + 2 * self.height
        print(f"triangle perimeter is {peri}")
        return peri

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        self.height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

if __name__ == "__main__":
    rp = RightPyramid(10,5)
    print(rp.area())