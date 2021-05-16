
arr = ['dog', 'cat', 'pikle']

for i in range(len(arr)):
    if i > -1:
        print(i, arr[i])
    else:
        print('lox')
print("----------")

for i, v in enumerate(arr):
    print(i, v)
