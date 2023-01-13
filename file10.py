def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    lst = data.split('\n')
    ans = []
    for i in lst:
        ans.append(len(i))
    return max(ans)
# Read data from file
f = open('txt_file/data10.txt', encoding='UTF-8')
data = f.read()
print(main(data))    

# Read data from file