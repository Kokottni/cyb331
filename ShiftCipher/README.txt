This directory has the shift cipher python code that was utilized in order to take any plaintext and convert it to a ciphertext and back. 

shiftcipher.py is the actual shift cipher that I implemented that will convert your plaintext.
This can be run by doing:
.\shiftcipher.py <enc (for encrypt) or dec (for decrypt)> <length of key to use> <-az (alphabet) or -b (binary)> <keyfile> <filetoshift> <filetooutputto>
                                            
hist.py will give you a histogram of the distribution of letters in the alphabet or binary from a given file
This can be run by doing:
.\hist.py <-az (for alphabet) -b (for binary)> <filetoread>
                                  
analyze.py is used to find certain statistics about your shifted data
It will give you a normalized IOC as we ll as the entropy of the data
This can be run by doing:
.\analyze.py <-az (for alphabet) -b (for binary)>
