sequences = [0, 1, 2, 3, 4, 5]
i = 0
while 1: #判斷條件值為1，代表迴圈永遠成立
    print(sequences[i], end='')
    i += 1
    if i == len(sequences):
        print('No elements left.')
        break