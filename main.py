n = int(input())
sequence = []
i = 1
while True:
    # extend the sequence list by the element "i" repeated i times
    sequence += [i] * i
    # if the length of the sequence is greater than or equal to n, print the first n elements of the sequence
    if len(sequence) >= n:
        print(*sequence[0:n])
        break
    i += 1
