given_data = (5, 6, 3, 9, 2, 12, 3, 8, 7)
listed = list(given_data)

print("주어진 리스트는 =", listed)

for k in range(1, len(listed)):
    for i in range(k, 0, -1):
        if listed[i] < listed[i - 1]:
            listed[i], listed[i - 1] = listed[i - 1], listed[i]
        
print("정렬된 결과는 :", listed)