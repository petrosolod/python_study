answer = []  # emty list

for _ in range(int(input())):  # how many string do we will check
    result = input()  # strings for check
    answer.append(result)  # use append for add all strings for check

look = input()  # word for seaching

for i in range(len(answer)):  # start iteration
    # we looking word from @look@ in our list by using indexes
    if look.lower() in answer[i].lower():
        print(*answer[i], sep='')
