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

# 16

def maps(a):
    result = []
    for number in a:
        result.append(number * 2)
    return result

# 17

def greet(name):
    return f"Hello, {name} how are you doing today?"

# 18 

def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return "even"
    elif sum(arr) % 2 != 0:
        return "odd"

# 19

def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count = 0
    total = 0
    
    for num in arr:
        if num > 0:
            count += 1
        elif num <= 0:
            total += num
    return [count,total]

# 20

def positive_sum(arr):
    if not arr:
        return 0
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total

# 21

def square_digits(num):
    result = ""
    
    for digit in str(num):
            result += str(int(digit) ** 2)
    return int(result)

# 22 

def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

# 23

def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    else:
        return False

# 24

def square(n):
    return n ** 2

# 25 

def basic_op(operator, value1, value2):
    if operator == "+" :
        return value1 + value2
    elif operator == "-" :
        return value1 - value2
    elif operator == "*" :
        return value1 * value2
    elif operator == "/":
        return value1 / value2