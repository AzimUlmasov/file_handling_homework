def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

    ans = []
    i = 0
    for num in data:
        if num.isdigit():
            i += 1
    ans.append(i)
    ans.append(len(data)- i)
    return ans

# Read data from file
f = open('txt_file/data05.txt', encoding='UTF-8')
data = f.read()
print(main(data))