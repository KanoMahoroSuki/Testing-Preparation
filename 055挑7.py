n = int(input())

print(sum(1 for i in range(1,n+1) if i % 7 == 0 or '7' in str(i)))