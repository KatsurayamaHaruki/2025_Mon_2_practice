import math
from rsa_0 import is_prime, gcd
from rsa_1 import generate_rsa_keys
from rsa_2 import encrypt_message
from rsa_3 import decrypt_message

# RSA暗号の実行デモンストレーション関数
def demonstrate_rsa():
    """
    RSA暗号の鍵生成、暗号化、復号のプロセスを実行し表示する。
    """
    print("RSA暗号のデモンストレーション 🔐")
    print("=" * 40)

    try:
        # デフォルトの素数と公開指数
        default_p, default_q, default_e = 61, 53, 17

        # 素数 p の入力
        prime_p_str = input(f"素数 p を入力してください (例: {default_p}, Enterでデフォルト値): ")
        prime_p = int(prime_p_str) if prime_p_str else default_p

        # 素数 q の入力
        prime_q_str = input(f"素数 q を入力してください (例: {default_q}, Enterでデフォルト値): ")
        prime_q = int(prime_q_str) if prime_q_str else default_q

        if not is_prime(prime_p):
            print(f"エラー: 入力された p ({prime_p}) は素数ではありません。")
            return
        if not is_prime(prime_q):
            print(f"エラー: 入力された q ({prime_q}) は素数ではありません。")
            return
        if prime_p == prime_q:
            print(f"エラー: p と q ({prime_p}) は異なる素数である必要があります。")
            return

        # φ(n) を計算し、ユーザーに e の選択の参考情報を提供する
        temp_phi_n = (prime_p - 1) * (prime_q - 1)
        print(f"\n計算された φ(n) = (p-1)*(q-1) = {temp_phi_n}.")
        print(f"公開指数 e は、1 < e < {temp_phi_n} であり、{temp_phi_n} と互いに素な数を選んでください。")
        print(f"(例: {default_e} は φ(n)={temp_phi_n} と互いに素です (gcd({default_e}, {temp_phi_n}) = {gcd(default_e, temp_phi_n)}))")

        # 公開指数 e の入力
        exponent_e_str = input(f"公開指数 e を入力してください (例: {default_e}, Enterでデフォルト値): ")
        exponent_e = int(exponent_e_str) if exponent_e_str else default_e
        print("-" * 20)

        # -- ステップ1: 鍵ペアの生成 --
        print("\nステップ1: 鍵ペアの生成中...")
        public_key, private_key = generate_rsa_keys(prime_p, prime_q, exponent_e)
        print("鍵ペアが生成されました:")
        print(f"  公開鍵 (e, n): ({public_key[0]}, {public_key[1]})")
        print(f"  秘密鍵 (d, n): (d は非表示, n={private_key[1]})") # dは秘密なので表示を工夫
        # print(f"  秘密鍵 (d, n): ({private_key[0]}, {private_key[1]})") # 学習用のため表示する場合はこちら
        print("=" * 40)

        # n の値が小さすぎる場合の警告
        if public_key[1] < 256: # n (public_key[1])
             print(f"警告: n ({public_key[1]}) が256未満です。標準的なASCII文字の暗号化に問題が生じる可能性があります。")

        # -- ステップ2: 暗号化するメッセージの入力 --
        message_to_encrypt = input("暗号化するメッセージを入力してください (例: Hello RSA!): ") or "Hello RSA!"
        print(f"\nステップ2: メッセージの暗号化")
        print(f"元のメッセージ: '{message_to_encrypt}'")
        print("-" * 20)

        # -- ステップ3: メッセージの暗号化 --
        encrypted_msg_blocks = encrypt_message(public_key, message_to_encrypt)
        print(f"暗号化されたメッセージ (数値ブロックのリスト):")
        print(encrypted_msg_blocks)
        print("=" * 40)

        # -- ステップ4: メッセージの復号 --
        print("\nステップ3: メッセージの復号")
        decrypted_msg = decrypt_message(private_key, encrypted_msg_blocks)
        print(f"復号されたメッセージ: '{decrypted_msg}'")
        print("-" * 20)

        # -- ステップ5: 結果の検証 --
        print("\nステップ4: 結果の検証")
        if message_to_encrypt == decrypted_msg:
            print("成功: 元のメッセージと復号されたメッセージは一致します。🎉")
        else:
            print("エラー: 元のメッセージと復号されたメッセージが一致しません。😭")

    except ValueError as ve:
        print(f"\nエラーが発生しました: {ve}")
    except Exception as e:
        print(f"\n予期せぬエラーが発生しました: {e}")

    print("=" * 40)
    print("RSA暗号のデモンストレーションを終了します。")

# メインの処理を実行
if __name__ == '__main__':
    demonstrate_rsa()