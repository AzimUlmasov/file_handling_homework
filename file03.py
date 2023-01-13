def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    ans = []
    for num in data:
        if num.isdigit():
            ans.append(num)
    return ans    
# Read data from file
f = open('txt_file/data03.txt', encoding='UTF-8')
data = f.read()
print(main(data))
