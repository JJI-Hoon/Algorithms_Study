import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
ans = n

for i in range(n):
    if a[i] - b > 0:
        ans += (a[i] - b) // c
        if (a[i] - b) % c:
            ans += 1
print(ans)