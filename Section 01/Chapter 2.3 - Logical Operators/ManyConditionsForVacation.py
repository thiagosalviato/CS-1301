
# Many conditions for vacation

# Conditions
can_afford = True
destination_is_safe = True
educational_value = True
relatives_nearby = True
is_international = False
have_passport = True
afraid_to_fly = False
have_a_car = False
is_a_beach = True
is_warm = False
has_skiing = True
is_a_city = True
is_off_peak = True
has_attraction = False


#Code is here!

#afford
pay = can_afford and destination_is_safe # first == true
parpay = destination_is_safe and (educational_value or relatives_nearby)
first = pay or parpay
#print(first)

#international
inter = is_international and have_passport and afraid_to_fly
notinter = not is_international and (have_a_car or not afraid_to_fly)
second = inter or notinter
#print(second)

#want
beach = is_a_beach and is_warm
skiing = has_skiing and not is_warm
tourist = is_a_city and is_off_peak or has_attraction
third = beach or skiing or tourist
#print(third)

# so we can go if all condition True
can_go = first and second and third
print(can_go)
