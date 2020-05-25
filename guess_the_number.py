# coding: utf-8
def game():
# prepare a sequence
    sequence = [i for i in range(101)]
    print(sequence)
# make choices from the sequence
    for _ in range(1):
        selection = choice(sequence)
        selection = int(selection)
    while True:
        n = input('What number am I thinking of man between 0 - 100: ')
        n = int(n)
        for i in range (1, 5):    
            if n - i == selection:
                print("very warm baby")
            if n + i == selection:
                print("very warm baby")
        for i in range (6, 10):
            if n - i == selection:
                print("gettin there, ay..warmer")
            if n + i == selection:
                print("gettin there, ay. warmer")
        if n > selection:
            print("go down")
        if n < selection:
            print("go up")
        if n == selection:
            print("Geez Louise, are ya irish?")
            break
            continue
            print("The end. Like and Subscribe!")
             
