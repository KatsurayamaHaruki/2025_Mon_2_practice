from rsa_0 import is_prime, gcd
import math
# 1. 鍵生成関数

def extended_gcd(a, b):
    """拡張ユークリッド互除法：ax + by = gcd(a, b) を満たす (gcd, x, y) を返す"""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(e, phi):
    """eのmod φにおける逆元（d）を求める"""
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("e_valとφ(n)は互いに素でなければなりません")
    return x % phi

def generate_rsa_keys(p, q, e_val):
    if p == q:
        raise ValueError("pとqは異なる素数でなければなりません")

    n = p * q
    phi_n = (p - 1) * (q - 1)

    if not (1 < e_val < phi_n):
        raise ValueError("e_valは1より大きく、φ(n)より小さくなければなりません")
    if math.gcd(e_val, phi_n) != 1:
        raise ValueError("e_valとφ(n)は互いに素でなければなりません")

    d = mod_inverse(e_val, phi_n)

    public_key = (e_val, n)
    private_key = (d, n)

    return public_key, private_key