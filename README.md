# Automated Cipher Solver
A program to automatically solve a simple substitution cipher using frequency analysis, built with Python using libraries such as Mat Plot Lib and Numpy and the OpenAI API.

# Installation and Setup
Clone this repository. You will need install python and all dependencies before hand.
To use the cipher solver, run main.py and follow the prompts for whatever simple substitution ciphertext you would like to decrypt. 

It may take multiple times, especially for smaller inputs.


# Testing Results
![alt text](https://github.com/cswmm/JakobsensCipherSolver/blob/main/keyAcc.png?raw=true)
![alt text](https://github.com/cswmm/JakobsensCipherSolver/blob/main/textAcc.png?raw=true)

Above is the result of testing the accuracy of the solver with respect to the number of characters in the ciphertext. With the text size, the decrypted plaintext accuracy increases linearly. In the end, this implementation was able to consistently achieve above 90% text decryption accuracy with large enough inputs.

Something interesting was the dip from 300 characters to 400 characters. 
Theoretically, accuracy should only increase with sample sizes. 
These tests were AI generated, though, which let to some similar phrases when it was the same sample size. 
While these samples were not deterministic, they also weren't truly random.

# Reflection
This project was just a way to automate my hopework in an information security class,
 where I had to solve this cipher somewhat by hand. 

One of the main challenges I ran into was debugging. 
I implemented the algorithm all at once, which at that point had so many moving parts it was a lot to 
dig through to find what was going wrong.

In the future, a more modular implementation would have been much easier for debugging. On top of this, my conventions were
a little messy in this project. While it was nice working solo, I wish I had spent more time learning python naming conventions
so to make cleaner code.

# Sources:
Jakobsen, Thomas. (1995). A fast method for cryptanalysis of substitution ciphers. Cryptologia. 19. 10.1080/0161-119591883944. 
