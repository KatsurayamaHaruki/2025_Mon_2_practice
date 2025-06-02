from rsa_0 import is_prime, gcd


# 3. 復号関数
def decrypt_message(private_key, encrypted_message_blocks):
    """
    秘密鍵を使って暗号文を復号する。
    private_key: (d, n) のタプル
    encrypted_message_blocks: 暗号化された数値のリスト
    復号: M = C^d mod n
    出力：数値のリストを複合して文字にして、結合した文字列
    """
    return 