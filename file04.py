def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    ans = []
    for num in data:
        if not num.isdigit():
            ans.append(num)
    return ans    
# Read data from file
f = open('txt_file/data04.txt', encoding='UTF-8')
data = f.read()
print(main(data))
