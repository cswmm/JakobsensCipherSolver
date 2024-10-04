from jakobsens import Solver

print('This solver may take multiple executions in order to fully decrypt the ciphertext')
print('Enter your ciphertext and continue to run the solver until it looks like decrypted English of some sort')
c = str(input('Enter ciphertext: '))
print()
solver = Solver(c)
while (True):
    print(solver.getPlaintext(solver.subSolver()))
    print()
    match = input('Is this the plaintext? (y/n): ')

    if (match != 'n'):
        print()
        print('ta daa')
        break