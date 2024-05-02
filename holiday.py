# defining the function for hotel cost
def hotel_cost(num_night):
    return num_night * 150 # assuming 150£ per night as cost

# defining another function for plane ticket cost
def plane_cost(city_flight):
    if city_flight == "london":
        return 500   # assuming ticket price 500£
    elif city_flight == "paris":
        return 600    # assuming ticket price 600£
    elif city_flight == "india":
        return 800  # assuming ticket price 800£
    else:
        return 400   # assuming default ticket price
    
# defining another function for renting car for sight_seeing
def car_rental(rental_days):
    return rental_days * 200  # assuming 200£ as per day cost

# defining all three function together 
def total_holiday_cost(num_night, city_flight,rental_days):
    total_cost = hotel_cost(num_night) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost  # calling all functions with their respective arguments

# print all the functions in readable way
def print_holiday_details(num_night, city_flight, rental_days):
    print("Number of Night at Hotel : " ,num_night)
    print("City for Flight : " , city_flight)
    print(" Number of Days for Car Rental : " , rental_days)

    total_cost = total_holiday_cost(num_night , city_flight, rental_days)
    print(" Total Holiday Cost is £" , total_cost)

# asking the user for input regarding number of nighta, city and days for car rental
num_night = int(input(" Enter the number of nights : "))
city_flight = input("Enter the Name of City : ")
rental_days = int(input("Enter the number of days for sight-seeing: "))

print_holiday_details(num_night, city_flight , rental_days)




