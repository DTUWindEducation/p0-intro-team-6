from functions import greet 
greet('world')

from functions import goldilocks 
goldilocks(180)

from functions import square_list
nums = [2, 3, 4]
result = square_list(nums)
print(result)

from functions import fibonacci_stop
result = fibonacci_stop(50)
print(result)

from functions import clean_pitch
pitch_angles = [20, 95, -5, 40]  
status_signals = [0, 1, 1, 0]  

result = clean_pitch(pitch_angles, status_signals)  # Correct usage
print(result)  


