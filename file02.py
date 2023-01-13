def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    lst = data.split(',')
    ans = 0
    for i in lst:
        ans += len(i)
    return ans    
# Read data from file
f = open('txt_file/data02.txt', encoding='UTF-8')
data = f.read()
print(main(data))
