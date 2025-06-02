# ヘルパー関数: 最大公約数 (GCD) を計算
def gcd(a, b):
    """2つの整数の最大公約数を計算する。"""
    while b:
        a, b = b, a % b
    return a

# ヘルパー関数: 素数判定 (簡易版)
def is_prime(n):
    """与えられた数が素数かどうかを判定する (簡易版)。"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True