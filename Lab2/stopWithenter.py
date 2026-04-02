import random, sys, select

def gen_infinite_sequence():
    while True:
        yield random.random()

numbers = gen_infinite_sequence()
for num in numbers:
    print(num)
    
    i, _, _ = select.select([sys.stdin], [], [], 0.01)
    if i: 
        sys.stdin.readline()  
        print("Stopped by me")
        break