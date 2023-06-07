#Program to find sum of first n natural number
#making a function to find sum
def calculate_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

#we need to find till first 10 natural numbers. So,n = 10
n = 10
result = calculate_sum(n)


print(result)
