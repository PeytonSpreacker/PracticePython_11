def getprime():
    ran = range(2,101)
    div = list()
    num = int(input('Pick a number: '))
    for i in ran:
        if num % i == 0:
            div.append(i)
        else:
            continue
    if len(div) < 3:
        print(num, 'is a prime number.')
    else:
        print(num, 'is not a prime number.')

getprime()