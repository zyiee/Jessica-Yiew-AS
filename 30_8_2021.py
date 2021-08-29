shapes = ['Rectangle','rectangle', 'Circle', 'circle', 'Triangle','triangle', 'Square', 'square','Parallelogram', 'parallelogram'] #list of shapes available to calculate
calc_type = ['Area', 'area', 'Perimeter', 'perimeter'] #area and perimeter options
rectangles = [shapes[0], shapes[1]]
circles = [shapes[2], shapes[3]]
triangles = [shapes[4], shapes[5]]
squares = [shapes[6], shapes[7]]
area = [calc_type[0], calc_type[1]]
perimeter = [calc_type[2], calc_type[3]]
history = {}

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

def app_dictionary(x):
    global results
    results = [op1, x]
    history[op2] = results
#--------------------------rectangle----------------------------
def r_base():
    global rec_base
    while True:
        try:
            rec_base = float(input('What is the base of your rectangle?\t'))
            break
        except ValueError:
            print('Please enter a number value')

def r_height():
    global rec_height
    while True:
        try:
            rec_height = float(input('What is the height of your rectangle?\t'))
            break
        except ValueError:
            print('Please enter a number value')

def rec_area(base,height):
    return base*height

def rec_peri(base, height):
    return 2*base + 2*height

def rectangle_function():
    r_base()
    r_height()
    if op1 in area:
        rectangle_area = rec_area(rec_height, rec_base)
        app_dictionary(rectangle_area)
        print('Area of rectangle:', rectangle_area)
    elif op1 in perimeter:
        rectangle_perimeter = rec_peri(rec_height, rec_base)
        app_dictionary(rectangle_peri)
        print('Perimeter of rectangle:', rectangle_perimeter)
        

if op2 in rectangles:
    rectangle_function()
    print(history)
#--------------------------circle----------------------------
