from rsa_0 import is_prime, gcd

# 1. 鍵生成関数
def generate_rsa_keys(p, q, e_val):
    """
    RSAの公開鍵と秘密鍵を生成する。
    p, q: 2つの異なる素数
    e_val: 公開指数 (1 < e_val < phi_n かつ phi_n と互いに素)
    出力：公開鍵 = (e_val, n) ←タプル形式
          秘密鍵 = (d, n) 
    """

    return 