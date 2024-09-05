from solver.jakobsens import subSolver


def main():

    input_file = 

    with open(input_file) as f:
        ciphertext = f.read().strip()

    s = subSolver(ciphertext)

    print(f"ciphertext:\n{ciphertext}")

    print(f"plaintext:\n{s.plaintext()}\n")