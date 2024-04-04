class Point:
    __match_args__ = ('x','y')
    def _init__(self, x, y):
        self.x = x 
        self.y = y 

match points:
    case[]:
        print("No points")
    case[Point(0,0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Signle point{x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")

# We can add an if clause to a pattern, know as a "guard"
match point: 
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")

# Subpatterns may be captured using the as keyword:
        case (Point(x1, y1), Point(x2, y2) as p2):....