from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

pt = b"Transfer Rp5000000 ke rekening 1234567890"
k, iv = get_random_bytes(16), get_random_bytes(16)
ct = AES.new(k, AES.MODE_CBC, iv).encrypt(pad(pt, 16))

dec = unpad(AES.new(k, AES.MODE_CBC, iv).decrypt(ct), 16)

ct_mod = bytearray(ct)
ct_mod[0] ^= 1 
dec_mod = AES.new(k, AES.MODE_CBC, iv).decrypt(ct_mod)

print(f"""=== HASIL EVALUASI SOAL 3 ===
[INFO ENKRIPSI]
Panjang Plainteks  : {len(pt)} byte
Panjang Cipherteks : {len(ct)} byte
Cipherteks (Hex)   : {ct.hex()}

[INFO DEKRIPSI]
Teks Hasil Dekripsi: {dec.decode()}
Sama dengan asli?  : {dec == pt}

[EFEK BIT FLIPPING]
Blok 1 (Hancur)    : {dec_mod[:16]}
Blok 2 (Berubah 1b): {dec_mod[16:32]}
Blok 3 (Normal)    : {dec_mod[32:]}
""")