from modules.timsort import timsort

n = int(input())
arr = [int(x) for x in input().split()]
print("Answer:",*timsort(arr,debug=True))
#Защита провалена
