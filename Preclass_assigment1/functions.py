###Exercies for week 0 in PiWE

#Ex 1
def greet(name):
    """Returns in terminal a greet to the given name"""
    return print(f"Hello, {name}!")

#Ex 2
def goldilocks(bed_size):
    """define if the bed_size is good for goldilocks standarts"""
    if bed_size < 140:
        print("Too small!")
    if bed_size > 150:
        print("Too large!")
    else:
        print("Just right. :)")

#3
def square_list(numbers):
    return [number ** 2 for number in numbers]
numbers = [2,3,9]
squared = square_list(numbers)
#print(squared)  # Output: [1, 4, 9, 16, 25]

#4
def fibonacci_stop(max_value):
    if max_value < 1:
        return []  # No Fibonacci numbers if the max value is less than 1
    
    fib_sequence = [1, 1]  # Start with the first two Fibonacci numbers
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > max_value:
            break
        fib_sequence.append(next_fib)
    
    return fib_sequence
#print(fibonacci_stop(4))

#5
def clean_pitch(pitch_angles, status_signals):
    cleaned_angles = []
    for pitch, status in zip(pitch_angles, status_signals):
        # If the pitch angle is out of range and the status signal is malfunctioning
        if (pitch < 0 or pitch > 90) and status > 0:
            cleaned_angles.append(-999)  # Set bad values to -999
        else:
            cleaned_angles.append(pitch)  # Keep good values untouched
    return cleaned_angles
pitch_angles = [30, 95, -10, 60, 45]
status_signals = [0, 1, 1, 0, 2]

cleaned = clean_pitch(pitch_angles, status_signals)
#print(cleaned)  # Output: [30, -999, -999, 60, 45]

