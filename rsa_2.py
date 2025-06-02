from rsa_0 import is_prime, gcd

# 2. 暗号化関数
def encrypt_message(public_key, plaintext_message):
    """
    公開鍵を使ってメッセージを暗号化する。
    public_key: (e, n) のタプル
    plaintext_message: 暗号化する文字列
    暗号化: C = M^e mod n
    出力：入力の文字列の文字を一文字ずつASCII値に変換し、暗号化した数字のリスト
    """
    return 
