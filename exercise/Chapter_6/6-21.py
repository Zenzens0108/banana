"""
If I borrow the power of Grok
"""
def decompress_string(src):
    if not src:
        return ''
    
    result = []
    i = 0
    while i < len(src):
        char = src[i]
        i += 1
        
        num = ''
        while i < len(src) and src[i].isdigit():
            num += src[i]
            i += 1
        count = int(num) if num else 1
        result.append(char * count)

    return ''.join(result)

print("src = ", end = "")
src = input()
output = decompress_string(src)
print(f"output = {output}")