#!/usr/bin/python3
import random

def stream_encrypt(data, key):
    """
    Params:
        data - byte string to undergo encryption
        key - key used for encryption
    Logic:
        create a key_Stream by generating a random number using key as seed
        for each character in data, take the xor of the character against the key_stream
        add the xor result to e
    Returns:
        e - the encrypted string from data
    """    
    e = bytes()
    random.seed(key)
    for i in range(len(data)):        
        k_stream = random.randint(0, 255)
        e += bytes([data[i] ^ k_stream])
    return e

def byte_scramble(data, key, unscramble = False):
    """
    Params:
        data - byte string to undergo encryption
        key - key used for encryption
    Logic:
        randomly generates a list of indices in length of data
        and appends bytes in new position from list of indices
        if unscramble, uses a dict to keep track of new indices to old indices
    Returns:
        e - the encrypted string from data
    """
    len_data = len(data)
    s = bytes()
    random.seed(key)
    new_pos = random.sample(range(0,len_data), len_data)
    if not unscramble:
        for i in range(len_data):        
            s += bytes([data[new_pos[i]]])
    else:
        d = dict()
        for i in range(len_data):
            d[new_pos[i]] = i
        for i in range(len_data):
            s += bytes([data[d[i]]])
    return s

def n_crypt(data, key, decrypt = False):
    """
    """
    e = data
    if decrypt:
        e = byte_scramble(e, key, unscramble=True)
        e = stream_encrypt(e, key)
    else:
        e = stream_encrypt(e, key)        
        e = byte_scramble(e, key)
    return e

if __name__ == "__main__":
    import custom_utils as cutils
    import sys
    # To test run
    # python n_crypt.py _random.txt key _random.ncrypt test/
    original_filename = sys.argv[1]
    key = sys.argv[2]
    output_filename = sys.argv[3]
    path = sys.argv[4]

    f = cutils.read_file(path+original_filename)
    
    cipher = bytes()    
    e = n_crypt(f, key)    
    cutils.write_file(e, path+output_filename)
    e = n_crypt(e, key, decrypt=True)
    cutils.write_file(e, path+"decrypted_"+original_filename)