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
    e_key, n_key = public_key
    encrypted_blocks = []
    for char_val in plaintext_message:
        m = ord(char_val)  # 文字をASCII値に変換 $M$
        # $M$ は $n_{key}$ より小さい必要がある。
        # 通常のASCII文字 (0-255) の場合、nが256以上なら問題ない。
        if m >= n_key:
            raise ValueError(
                f"メッセージの文字 '{char_val}' (ASCII値: {m}) は n ({n_key}) より大きいため暗号化できません。"
                "より大きな素数 p, q を選択してください。"
            )
        # 暗号化: C = M^e mod n
        c = pow(m, e_key, n_key)
        encrypted_blocks.append(c)
    return encrypted_blocks
