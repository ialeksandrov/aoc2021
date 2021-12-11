data = [int(x) for x in open("input_01.txt", 'r')]
print(sum([data[i] > data[i -1] for i in range(1, len(data))]))
print(sum([data[i] > data[i -3] for i in range(1, len(data))]))