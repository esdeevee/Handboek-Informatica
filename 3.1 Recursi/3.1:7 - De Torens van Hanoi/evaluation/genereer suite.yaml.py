def hanoi(n):
    if n == 1:
        return 1
    else:
        return hanoi(n-1) + 1 + hanoi(n-1)


# suite.yaml voor de TESTed judge
# wis alle gegevens in suite.yaml
file = open("suite.yaml", "w")
file.truncate()
file.close()

with open('suite.yaml', 'a') as file:
    file.write('- tab: "hanoi"\n')
    file.write('  testcases:\n')
    for i in range(1, 26):
        file.write('    - expression: "hanoi(' + str(i) + ')"\n')
        file.write('      return: ' + str(hanoi(i)) + '\n')
    
