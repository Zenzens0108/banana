"""
Grok Grok
"""
text = input("문자열을 입력하시오 : ")

alphabet = "".join(char.lower() for char in text if char.isalpha())

if alphabet == alphabet[:-1]:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")