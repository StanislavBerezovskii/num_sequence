n = int(input())
sequence = []
i = 1
while True:
    sequence += [i] * i
    if len(sequence) >= n:
        print(*sequence[0:n])
        break
    i += 1
