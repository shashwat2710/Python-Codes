'''Snippet Code to convert every character to string'''
def to_str(bytes_or_str):
    '''Convert to String'''
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

if __name__ == "__main__":
    output = to_str("")
    print(output)
