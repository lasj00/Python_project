while True:
    try:
        x = int(input('Please enter a number: '))
        break
    except (KeyboardInterrupt, ValueError):
        print('Not a number, please try again')

print('I got: ' + str(x))