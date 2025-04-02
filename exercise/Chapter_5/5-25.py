"""
숭배합니다 GROK이시여
"""
s1 = 'Kang Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'

def transform_string(s):
    return s.replace(" ", "").replace("-", "").upper()

new_s1 = transform_string(s1)
new_s2 = transform_string(s2)
new_s3 = transform_string(s3)
new_s4 = transform_string(s4)

print(f"{s1}(은)는 {new_s1}(으)로 수정됨")
print(f"{s2}(은)는 {new_s2}(으)로 수정됨")
print(f"{s3}(은)는 {new_s3}(으)로 수정됨")
print(f"{s4}(은)는 {new_s4}(으)로 수정됨")

print(f"{new_s1}: {new_s1.count('N')} 개의 N이 나타남")
print(f"{new_s2}: {new_s2.count('N')} 개의 N이 나타남")
print(f"{new_s3}: {new_s3.count('N')} 개의 N이 나타남")
print(f"{new_s4}: {new_s4.count('N')} 개의 N이 나타남")