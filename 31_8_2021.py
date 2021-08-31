shapes = ['Rectangle','rectangle', 'Circle', 'circle', 'Triangle','triangle', 'Square', 'square','Parallelogram', 'parallelogram'] #list of shapes available to calculate
calc_type = ['Area', 'area', 'Perimeter', 'perimeter'] #area and perimeter options
#list of different spelled words for validation
rectangles = [shapes[0], shapes[1]]
circles = [shapes[2], shapes[3]]
triangles = [shapes[4], shapes[5]]
squares = [shapes[6], shapes[7]]
area = [calc_type[0], calc_type[1]]
perimeter = [calc_type[2], calc_type[3]]
history = {} #dictionary to record calculator history

def a_p(): #asks user if area or perimeter is to be calculated
    global op1 
    op1 = str(input('Welcome to the area perimeter calculator. \nWould you like to calculate the area or perimeter?\t'))
    if op1 not in calc_type:
        print('Please enter either area or perimeter.')
        a_p()
    else:
        print(op1, 'has been selected.')
a_p()

def s_s(): #asks user which shape to calculate
    global op2
    op2 = str(input('What shape would you like to calculate the ' + op1 + ' of?\nShapes available are: Rectangle, Circle, Triangle, Square, Parallelogram\n'))
    if op2 not in shapes:
        print('Please choose from the given list.')
        s_s()
    else:
        print(op2, 'has been selected.')
s_s()

#consider adding in user input values for calculation
def app_dictionary(x): #appends calculation results into dictionary
    global results
    results = [op1, x]
    history[op2] = results
#--------------------------rectangle----------------------------
def r_base(): #user input for rectangle base
    global rec_base
    while True:
        try:
            rec_base = float(input('What is the base of your rectangle?\t'))
            break
        except ValueError:
            print('Please enter a number value')

def r_height(): #user input for rectangle height
    global rec_height
    while True:
        try:
            rec_height = float(input('What is the height of your rectangle?\t'))
            break
        except ValueError:
            print('Please enter a number value')

def rec_area(base,height): #calculates area of rectangle
    return base*height

def rec_peri(base, height): #calculates perimeter of rectangle
    return 2*base + 2*height

def rectangle_function(): #a full function which includes: user input for dimensions, calculating area and perimeter of rectangle and appending into history dictionary
    r_base()
    r_height()
    if op1 in area:
        rectangle_area = rec_area(rec_height, rec_base)
        app_dictionary(rectangle_area)
        print('Area of rectangle:', rectangle_area)
    elif op1 in perimeter:
        rectangle_perimeter = rec_peri(rec_height, rec_base)
        app_dictionary(rectangle_perimeter)
        print('Perimeter of rectangle:', rectangle_perimeter)
        

if op2 in rectangles: #if a rectangle is to be calculated, if statement leads code to rectangle_function()
    rectangle_function()
    print(history)
#--------------------------circle----------------------------
def circ_length(): #user input for circle radius
    global circ_radius
    print('Radius of circle is half of radius length')
    while True:
        try:
            circ_radius = float(input('What is the radius of your circle?\t'))
            break
        except ValueError:
            print('Please enter a number value')
            
pi = 3.141592

def circ_area(radius): #calculates area of circle
    return pi*(circ_radius**2)

def circ_perimeter(radius): #calculates perimeter of circle
    return 2*pi*radius

def circle_function(): #a full function which includes: user input for radius, calculating area and perimeter of circle and appending it to history dictionary
    circ_length()
    if op1 in area:
        circle_area = circ_area(circ_radius)
        app_dictionary(circle_area)
        print('Area of circle:', circle_area)
    elif op2 in perimeter:
        circle_perimeter = circ_perimeter(circ_radius)
        app_dictionary(circle_area)
        print('Perimeter of circle:', circle_perimeter)

if op2 in circles: #if a circle is to be calculated, if statement leads code to circle_function()
    circle_function()
    print(history)
#--------------------------triangle----------------------------
def triangle_base():
    global tri_base
    while True:
        try:
            tri_base = float(input('What is the base length of your triangle?\t'))
            break
        except ValueError:
            print('Please enter a number value')

def triangle_height():
    global tri_height
    while True:
        try:
            tri_height = float(input('What is the height length of your triangle?\t'))
            break
        except ValueError:
            print('Please enter a number value')

def triangle_side():
    global tri_side
    while True:
        try:
            tri_side = float(input('What is the side length of your triangle?\t'))
            break
        except ValueError:
            print('Please enter a number value')

def triangle_side_2():
    global tri_side_2
    while True:
        try:
            tri_side_2 = float(input('What is the 2nd side length of your triangle?\t'))
            break
        except ValueError:
            print('Please enter a number value')

def triangle_area(base, height):
    return 0.5*base*height

def triangle_perimeter(base, side, side_2):
    return base + side + side_2

def triangle_area_function():
    triangle_base()
    triangle_height()
    tri_area = triangle_area(tri_base, tri_height)
    app_dictionary(tri_area)
    print('Area of triangle:', tri_area)

def triangle_perimeter_function():
    triangle_base()
    triangle_side()
    triangle_side_2()
    tri_perimeter = triangle_perimeter(tri_base, tri_side, tri_side_2)
    app_dictionary(tri_perimeter)
    print('Perimeter of triangle:', tri_perimeter)

if op2 in triangles and area:
    triangle_area_function()
    print(history)
elif op2 in triangles and perimeter:
    triangle_perimeter_function()
    print(history)
#--------------------------square----------------------------                     
def square_base():
    global sq_base
    while True:
        try:
            sq_base = float(input('What is the base of your square?\t'))
            break
        except ValueError:
            print('Please enter a number value')

def square_height():
    global sq_height
    while True:
        try:
            sq_height = float(input('What is the height of your square?\t'))
            break
        except ValueError:
            print('Please enter a number value')

def rec_area(base,height): #calculates area of square - same formula can be used
    return base*height

def rec_peri(base, height): #calculates perimeter of square - same formula can be used
    return 2*base + 2*height

def square_function():
    square_height()
    square_base()
    if op1 in area:
        square_area = rec_area(sq_base, sq_height)
        app_dictionary(square_area)
        print('Area of square:', square_area)
    elif op1 in perimeter:
        square_perimeter = rec_perimeter(sq_base, sq_height)
        app_dictionary(square_perimeter)
        print('Perimeter of square:', square_perimeter)

if op2 in squares:
    square_function()
    print(history)