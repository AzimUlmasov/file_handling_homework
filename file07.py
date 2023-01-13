def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    i = 0
    for num in data:
        if num.isdigit():
            i += int(num)
    return i   
# Read data from file
f = open('txt_file/data07.txt', encoding='UTF-8')
data = f.read()
print(main(data))