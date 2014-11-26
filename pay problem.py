#Tavonga Mudzana
#24/11/14
#funtcion_total pay calculation

#calculate overtime pay should do the following:
    #work ut how many hours over 40  that they have worked
    #find out the total for the basic hours worked


#calculate total pay
def calculate_basic_pay(hours,rate):
    total=hours*rate
    return total

#calculate overtime pay
def calculate_overtime_pay(hours,rate):
    overtime_hours=hours-40
    basic_pay=40*rate
    overtime_pay=ovetime-hours*(rate*1.5)
    total=basic_pay + overtime_pay
    return total

def calculate_total_pay(hours,rate):
    if hours<=40:
        total=calculate_basic_pay(hours,rate)
    else:
        total=calculate_overtime_pay(hours,rate)
    return total    
        
def hours_and_rate():
    hours=int(input("please enter the number of hours worked: "))
    rate=int(input("please enter the rate: "))
    return hours
    return rate

def display_total_pay(total):
    total=calculate_total_pay(hours,rate)
    return total

def calculate_pay():
    total=display_total_pay(total)
    return total

hours_rate=hours_and_rate()
total_pay=calculate_pay()
print(total_pay)
                    
