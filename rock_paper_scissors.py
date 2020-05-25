def knh():
    number = [i for i in range(1, 4)]
    for _ in range(1):
        hand = choice(number)
        key = int(hand)
    while True:
        me = input('Which one is it?: ')
        me = str(me)
        if me == rps[key]:
            print("draw")
        if me == 'scissors':
            if rps[key] == 'paper':
                print("win!")
            if rps[key] == 'rock':
                print("looooser!")
        if me == 'rock':
            if rps[key] == 'paper':
                print("looooser!")
            if rps[key] == 'scissors':
                print("win!")
        if me == 'paper':
            if rps[key] == 'rock':
                print("win!")
            if rps[key] == 'scissors':
                print("looooser!")
        break