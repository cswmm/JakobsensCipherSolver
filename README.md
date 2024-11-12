# Automated Cipher Solver
A program to automatically solve a simple substitution cipher using frequency analysis, build with Python using Mat Plot Lib and Numpy.

# Testing Results
![alt text](https://github.com/cswmm/JakobsensCipherSolver/blob/main/keyAcc.png?raw=true)
![alt text](https://github.com/cswmm/JakobsensCipherSolver/blob/main/textAcc.png?raw=true)
Above is the result of testing the accuracy of the solver with respect to the number of characters in the ciphertext.

# Installation and Setup
Clone this repository. You will need Mat Plot Lib and Numpy installed.
To use the cipher solver, run main.py and follow the prompts for whatever simple substitution ciphertext you would like to decrypt. 

It may take multiple times, especially for smaller inputs.

# Reflection
This project was just a fun idea I had while doing hopework in an information security class, where I had to solve this cipher by hand. I knew there must be a better way of doing it, or at least a way to automate it, so I decided to implement Jakobsen's algorithm.

I set out to build a tool to do my homework for me, essentially, but also a way to get some Python experience and apply what I have been self teaching recently.

One of the main challenges I ran into was debugging. I implemented the algorithm all at once, which at that point had so many moving parts it was a lot to dig through to find what was going wrong.

At the end of the day, this project used Python and libraries such as Mat Plot Lib and Numpy. In the next iteration I plan on applying more OOP design principles and testing incrementally to quicken the design process.


# Sources:
Jakobsen, Thomas. (1995). A fast method for cryptanalysis of substitution ciphers. Cryptologia. 19. 10.1080/0161-119591883944. 
