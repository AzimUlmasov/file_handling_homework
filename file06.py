def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    lst = data.split('\n')
    ans = []
    for i in lst:
        ans.append(len(i))
    return ans
# Read data from file
f = open('txt_file/data06.txt', encoding='UTF-8')
data = f.read()
print(main(data))