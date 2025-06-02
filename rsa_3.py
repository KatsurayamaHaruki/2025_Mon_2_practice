def decrypt_message(private_key, encrypted_message_blocks):
    """
    秘密鍵を使って暗号文を復号する。
    
    Parameters:
    - private_key: (d, n) のタプル
    - encrypted_message_blocks: 暗号化された数値のリスト
    
    復号方法:
    - 各ブロック C に対して M = C^d mod n を計算し、M を文字に変換
    
    Returns:
    - 復号された文字列
    """
    d, n = private_key
    decrypted_chars = [chr(pow(c, d, n)) for c in encrypted_message_blocks]
    return ''.join(decrypted_chars)
