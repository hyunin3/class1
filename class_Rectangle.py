class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(Point):
    
    def __init__(self, po1, po2):
        self.po1 = po1
        self.po2 = po2
                
    def get_area(self):
        area = abs(self.po1.x - self.po2.x) * abs(self.po1.y - self.po2.y)
        return area
        
    def get_perimeter(self):
        perimeter = abs(self.po1.x - self.po2.x) * 2 + abs(self.po1.y - self.po2.y) * 2
        return perimeter
         
    def is_square(self):
        if abs(self.po1.x - self.po2.x) != abs(self.po1.y - self.po2.y):
            return False
        else:
            return True
                
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())        #4 넓이
print(r1.get_perimeter())   #8 둘레
print(r1.is_square())      #True 정사각형 유무

p3 = Point(3, 7)            
p4 = Point(6, 4)            
r2 = Rectangle(p3, p4)      
print(r2.get_area())        #9
print(r2.get_perimeter())   #12
print(r2.is_square())      #True

