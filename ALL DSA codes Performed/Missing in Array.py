n = int(input())

arr = list(map(int, input().split()))

total_sum = n*(n+1)//2

actual_sum = sum(arr)

missing_number = total_sum - actual_sum
print(missing_number)
