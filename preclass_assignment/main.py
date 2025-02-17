###Testiong the function
from functions import *
import random

#Testing greet
greet("Donald Duck")

#Testing goldilock
too_big = 151
too_small = 139
just_right = 145

print(f"The result for {too_big} is : ", end='')
goldilocks(too_big)

print(f"The result for {too_small} is : ",end='')
goldilocks(too_small)

print(f"The result for {just_right} is : ", end="")
goldilocks(just_right)

#testing square list
list_to_square = list(range(1,20,3))
print(f"Intial list: {list_to_square}")
print(f"Squared list: {square_list(list_to_square)}")

#testing fibonacci_stop
max_nb = 16.49
print(f"for the max={max_nb} the list is: {fibonacci_stop(max_nb)}")

low_nb = -5
print(f"for the max={low_nb} the list is: {fibonacci_stop(low_nb)}")

exact_nb = 13
print(f"for the max={exact_nb} the list is: {fibonacci_stop(exact_nb)}")

#test of clean_pitch
rd_measurement = random.sample(range(-2,93), 10)
rd_signal = random.choices([0,1], k=10)

print(f"For measurement: {rd_measurement}")
print(f"and theses signal status: {rd_signal}")
print(f"The cleaned picth is {clean_pitch(measurement=rd_measurement, status=rd_signal)}")
