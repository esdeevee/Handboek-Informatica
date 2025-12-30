def hanoi(n):
    if n == 1:
        return 1
    else:
        return hanoi(n-1) + 1 + hanoi(n-1)
