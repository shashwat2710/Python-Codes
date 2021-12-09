'''Snippet Code to convert every character to byte value.'''
def to_bytes(bytes_or_str):
    '''Convert to String'''
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

if __name__ == "__main__":
    output = to_bytes("ABCD")
    print(output)
