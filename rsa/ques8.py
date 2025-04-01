from Crypto.Util.number import inverse

e = 3
n = 742449129124467073921545687640895127535705902454369756401331
ciphertext = 39207274348578481322317340648475596807303160111338236677373
p = 752708788837165590355094155871
q = 986369682585281993933185289261

phi_n = (p - 1) * (q - 1)
private_key = inverse(e, phi_n)
decrypted_int = pow(ciphertext, private_key, n)
decoded_message = bytes.fromhex(format(decrypted_int, 'x')).decode('utf-8')

print("Decrypted message:", decoded_message)