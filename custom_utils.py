#!/usr/bin/python3

def read_file(data_file):
    """
    Params:
        data_file - path and name to file to be read
    Returns:
        returns a byte object of the file
    """
    with open(data_file, 'rb') as f:
        data = f.read()
    f.close()    
        
    return data

def write_file(data, file_name):
    """
    Params:
        data - data to write to file
        file_name - name of file
    Logic:
        writes cipher_text to a file named ss_key_cipher_encryption
    """    
    with open(file_name, 'wb') as f:
        f.write(data)
    f.close()    


if __name__ == "__main__":
    def test_read_file():
        """
        Unit test for read_file()
        """
        data = read_file('sub_transpose.py')        
        print(data)
        return
    test_read_file()
    pass