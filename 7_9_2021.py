shapes = ['Rectangle','rectangle', 'Circle', 'circle', 'Triangle','triangle', 'Square', 'square','Parallelogram', 'parallelogram'] #list of shapes available to calculate
calc_type = ['Area', 'area', 'Perimeter', 'perimeter'] #area and perimeter options
#list of different spelled words for validation
rectangles = [shapes[0], shapes[1]]
circles = [shapes[2], shapes[3]]
triangles = [shapes[4], shapes[5]]
squares = [shapes[6], shapes[7]]
parallelograms = [shapes[8], shapes[9]]

area = [calc_type[0], calc_type[1]]
perimeter = [calc_type[2], calc_type[3]]

yes_no = ['Yes', 'yes', 'Y', 'y', 'No', 'no', 'N', 'n']
yes = ['Yes', 'yes', 'Y', 'y']
no = ['No', 'no', 'N', 'n']

history = {} #dictionary to record calculator history
pi = 3.141592

def a_p(): #asks user if area or perimeter is to be calculated
    op1 = str(input('Welcome to the area perimeter calculator. \nWould you like to calculate the area or perimeter?\t'))
    if op1 not in calc_type:
        print('Please enter either area or perimeter.')
        a_p()
    else:
        print(op1, 'has been selected.')
    return op1

def s_s(): #asks user which shape to calculate
    op2 = str(input('What shape would you like to calculate the ' + op1 + ' of?\nShapes available are: Rectangle, Circle, Triangle, Square, Parallelogram\n'))
    if op2 not in shapes:
        print('Please choose from the given list.')
        s_s()
    else:
        print(op2, 'has been selected.')
    return op2

#consider adding in user input values for calculation
def app_dictionary(answer): #appends calculation results into dictionary
    global key
    key = str(op2 + ' ' + op1)
    history[key] = answer

def number_check(question):
    while True:
        try:
            user_input = float(input(question))
            break
        except ValueError:
            print('Please enter a number value')
    return user_input

#def restrict(shape_type, shape_function):
    #if op2 in shape_type:
        #shape_function


def rectangle_function():
    user_input = number_check('What is the base of your rectangle?\t')
    rec_base = user_input
    user_input = number_check('What is the height of your rectangle?\t')
    rec_height = user_input
    
    rec_area = rec_base*rec_height
    rec_perimeter = 2*rec_base + 2*rec_height
    if op1 in area:
        print('Area of rectangle:', rec_area)
        app_dictionary(rec_area)
    elif op1 in perimeter:
        print('Perimeter of rectangle:', rec_perimeter)
        app_dictionary(rec_perimeter)

def circle_function():
    print('Radius is 1/2 the length of diameter.\t')
    user_input = number_check('What is the radius of your circle?\t')
    circ_radius = user_input
    
    circ_area = pi*(circ_radius**2)
    circ_perimeter = 2*pi*circ_radius
    if op1 in area:
        print('Area of circle:', circ_area)
        app_dictionary(circ_area)
    elif op1 in perimeter:
        print('Perimeter of circle:', circ_perimeter)
        app_dictionary(circ_perimeter)

def triangle_function():
    if op1 in area:
        user_input = number_check('What is the base of your triangle?\t')
        tri_base = user_input
        user_input = number_check('What is the height of your triangle?\t')
        tri_height = user_input
        tri_area = 0.5*tri_base*tri_height
        print('Area of triangle:', tri_area)
        app_dictionary(tri_base_a, tri_height_a, tri_area)
    elif op1 in perimeter:
        print('What are the 3 sides of your triangle?')
        user_input = number_check('Side 1:\t')
        side_1 = user_input
        user_input = number_check('Side 2:\t')
        side_2 = user_input
        user_input = number_check('Side 3:\t')
        side_3 = user_input
        tri_perimeter = side_1 + side_2 + side_3
        print('Perimeter of triangle:', tri_perimeter)
        app_dictionary(tri_perimeter)

def square_function():
    user_input = number_check('What is the height of your square?\t')
    sq_height = user_input
    user_input = number_check('What is the base of your square?\t')
    sq_base = user_input
    
    sq_area = sq_height*sq_base
    sq_perimeter = (2*sq_height) + (2*sq_base)
    if op1 in area:
        print('Area of square:', sq_area)
        app_dictionary(sq_area)
    elif op1 in perimeter:
        print('Area of perimeter:', sq_perimeter)
        app_dictionary(sq_perimeter)

def parallelogram_function():
    if op1 in area:
        user_input = number_check('What is the base of your parallelogram?\t')
        par_base = user_input
        user_input = number_check('What is the height of your parallelogram?\t')
        par_height = user_input
        par_area = par_base*par_height
        print('Area of parallelogram:', par_area)
        app_dictionary(par_area)
    if op1 in perimeter:
        user_input = number_check('What is the base of your parallelogram?\t')
        par_base_2 = user_input
        user_input = number_check('What is the side of your parallelogram?\t')
        par_side = user_input
        par_perimeter = 2*(par_base_2 + par_side)
        print('Perimeter of parallelogram:\t')
        app_dictionary(par_perimeter)

#def calculator():
    #a_p()
    #s_s()
    #restrict(rectangles, rectangle_function())
    #restrict(circles, circle_function())
    #restrict(triangles, triangle_function())
    #restrict(squares, square_function())
    #restrict(parallelograms, parallelogram_function())

def calculator():
    if op2 in rectangles:
        rectangle_function()
    elif op2 in circles:
        circle_function()
    elif op2 in triangles:
        triangle_function()
    elif op2 in squares:
        square_function()
    elif op2 in parallelograms:
        parallelogram_function()

   
op1 = a_p()
op2 = s_s()
num = 1
calculator()
more = str(input('Would you like to calculate more?'))
while more in yes:
    op1 = a_p()
    op2 = s_s()        
    calculator()
    more = str(input('Would you like to calculate more?'))

if more in no:
    print('Thank')
    print(history)
elif more not in yes_no:
    print('Please enter either yes or no')




    


            
