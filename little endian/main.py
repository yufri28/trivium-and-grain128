import time

from trivium import Trivium
from trivium import hex_to_bits, bits_to_hex, bit_to_ascii, str_to_bits


def main():
    # Key IV are little endian bits
    KEY = str_to_bits("adrian")[::-1]
    IV = str_to_bits("adrian")[::-1]

    # Encoding a string
    trivium_encoder = Trivium(KEY, IV)
    cipher = trivium_encoder.encrypt("Secara umum ada dua tipe algoritma kriptografi berdasarkan kuncinya yaitu algoritma simetris dan algoritma asimetris. ElGamal adalah sebuah algoritma untuk kriptografi kunci publik atau asimetris. Algoritma asimetris terdiri atas dua buah kunci yaitu kunci publik untuk melakukan enkripsi sedangkan kunci pribadi untuk melakukan dekripsi. Algoritma asimetris terdiri atas dua buah kunci yaitu kunci publik untuk melakukan enkripsi sedangkan kunci pribadi untuk melakukan dekripsi. Algoritma ElGamal biasanya digunakan untuk enkripsi data berupa teks saja. Skripsi ini menguraikan bagaimana menerapkan algoritma ElGamal pada file citra 2 dimensi. Algoritma ini menggunakan beberapa persamaan untuk melakukan proses generate key, proses enkripsi dan proses dekripsi. Citra yang akan di enkripsi ke algoritma ini adalah plain citra grayscale. Modifikasi yang dilakukan adalah dengan mengubah kunci public g dan z menjadi representasi data 2 dimensi, dengan g merupakan citra grayscale dan z adalah citra RGB. Hasil akhir menunjukkan bahwa enkripsi berhasil dilakukan dengan nilai koefisien korelasi antara citra plain dan chipper berada pada nilai kurang dari satu.")

    # Cipher texts are little endian bits
    print("Encoded:", bits_to_hex(cipher)[::-1])
    print("Encoded:", bit_to_ascii(cipher)[::-1])

    # Decoding from the cipher
    trivium_decoder = Trivium(KEY, IV)
    plain = trivium_decoder.decrypt(cipher)

    # Plain Text
    print("Decoded:", plain)


if __name__ == "__main__":
    main()
