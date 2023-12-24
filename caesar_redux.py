
###########################################################
# Caesar Redux                                            #
###########################################################
# The Caesar cipher is a simple encryption technique that #
# was used by Julius Caesar to send secret messages to    #
# his allies. It works by shifting the letters in the     #
# plaintext message by a certain number of positions.     #
# Decryption is performed by shifting in the opposite     #
# direction by the same number of positions.              #
#                                                         #
# A program that implements this technique is needed to   #
# encrypt a plaintext message or decrypt a ciphertext     #
# messages. Spaces are not affected by encryption or      #
# decryption.                                             #
#                                                         #
# You need to determine whether the value that is         #
# provided is plaintext or ciphertext. If the value       #
# provided is plaintext, you should output the encrypted  #
# message given the shift value above. If the provided    #
# value is ciphertext, you should output the decrypted    #
# message.                                                #
#                                                         #
###########################################################

A_POS = ord("a")
Z_POS = ord("z")
LETTER_RANGE = Z_POS - A_POS + 1
KEYWORD = "the"

def pos_mod(val, mod):
    val %= mod
    if val < 0:
        val += mod
    return val

def shift_char(c, shift):
    global A_POS
    global Z_POS
    global LETTER_RANGE
    
    char_pos = ord(c)
    if char_pos < A_POS or char_pos > Z_POS:
        return c
        
    char_pos_offset = char_pos - A_POS
    shifted_pos_offset = char_pos_offset + shift
    
    shifted_pos_offset = pos_mod(shifted_pos_offset, LETTER_RANGE)
        
    shifted_pos = shifted_pos_offset + A_POS
    s = chr(shifted_pos)
    return s
    

def enc(k, msg):
    cphr = ""
    for c in msg:
        cphr += shift_char(c, -k)
    return cphr

def dec(k, cphr):
    return enc(-k, cphr)

n = int(input())

for i in range(n):
    k = int(input())
    line = input()
    words = line.split(" ")
    
    answr = None
    if KEYWORD in words:
        answr = enc(k, line)
    else:
        answr = dec(k, line)
        
    print(answr)