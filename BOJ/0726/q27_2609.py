# GCD & LCM

def euclidian_gcd(m, n):
    if m < n:
        m, n = n, m         # m(dividend)를 큰 수로 유지
    if m % n == 0:          # m이 n으로 나누어진다면 n자체가 최대공약수
        return n        
    else:                   
        return euclidian_gcd(n, m%n)  # 왜 나머지로 나누는 것일까?

N1,N2 = map(int, input().split())

print('%d\n%d'%(euclidian_gcd(N1,N2), N1*N2//euclidian_gcd(N1,N2)))