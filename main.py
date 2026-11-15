# 1 Convert a Boolean to a String

def boolean_to_string(b):
    return str(b)

# 2

def opposite(number):
    return -number

# 3 

def double_integer(i):
    return i + i

# 4

def number_to_string(num : int) -> str:
    return str(num)

# 5

def sum_array(a):
    return sum(a)

# 6

def switch_it_up(number):
    if number == 1: 
        return("One")
    elif number==2:
        return("Two")
    elif number==3:
        return("Three")
    elif number==4:
        return("Four")
    elif number==5:
        return("Five")
    elif number==6:
        return("Six")
    elif number==7:
        return("Seven")
    elif number==8:
        return("Eight")
    elif number==9:
        return("Nine")
    elif number==0:
        return "Zero"

# 7 

def better_than_average(class_points, your_points):
    average_score = sum(class_points) / len(class_points)
    if your_points > average_score:
        return True
    else: return False

# 8

def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"
    else: return "Keep at it until you get it"

# 9

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0

# 10

def is_even(n): 
    if n % 2 == 0:
        return True
    else:
        return False

# 11

def unusual_five():
    return len("ptprp")

# 12 

def string_to_number(s):
    return int(s)

# 13

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
    if a == b:
        return a

# 14

def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    elif flower2 % 2 == 0 and flower1 % 2 != 0:
        return True
    else:
        return False

# 15

def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"