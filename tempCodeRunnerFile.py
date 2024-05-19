class Rectangle:
    def __init__(self, color, length=10, width=7):
        self.color = color
        self.length = length
        self.width = width

rectangle1 = Rectangle('green')
rectangle2 = Rectangle('purple', width=5, length=1)
rectangle3 = Rectangle('black', length=4, width=9)

print(rectangle1.length, rectangle1.width)
print(rectangle2.length, rectangle2.width)
print(rectangle3.length, rectangle3.width)