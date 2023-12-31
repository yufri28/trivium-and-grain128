import package
import matplotlib.pyplot as plt
import time


def visualize_text_grain128(key_str, title, path_plainteks, path_cipherteks, path_cipher_ascii, path_cipher_hex):

    with open(path_plainteks, 'r', encoding='latin-1') as file:
        plaintext = file.read()

    key_bits = ''.join(format(ord(c), '08b') for c in key_str)

    key = [int(bit) for bit in key_bits]

    grain128 = package.Grain128(key)

    # Enkripsi
    block_size = 80
    plaintext_blocks = grain128.split_into_blocks(plaintext, block_size)

    list_ciphertext = []
    list_ciphertext_hex = []
    list_ciphertext_ascii = []

    # Hitung waktu eksekusi
    timer = Timer()
    timer.start()
    for i, block in enumerate(plaintext_blocks):
        ciphertext = grain128.encrypt(block, key)
    timer.stop()
    print(f"Durasi waktu eksekusi {title}:" +
          " {:.9f} detik".format(timer.get_duration()))
    # Cetak blok-blok hasil pembagian
    for i, block in enumerate(plaintext_blocks):
        ciphertext = grain128.encrypt(block, key)
        ciphertext_str = ''.join(str(bit) for bit in ciphertext)
        ciphertext_hex = hex(int(ciphertext_str, 2))[
            2:].zfill(len(ciphertext_str) // 4)
        ciphertext_ascii = ''.join(
            [chr(int(ciphertext_str[i:i+8], 2)) for i in range(0, len(ciphertext_str), 8)])

        # print(f"Ciphertext Blok {i+1}: {ciphertext_ascii}")
        list_ciphertext.append(ciphertext)
        list_ciphertext_hex.append(ciphertext_hex)
        list_ciphertext_ascii.append(ciphertext_ascii)

    # decrypted_text = []
    # for i, block in enumerate(list_ciphertext):
    #     decrypted_plaintext = grain128.decrypt(block, key)
    #     decrypted_plaintext_str = ''.join(
    #         str(bit) for bit in decrypted_plaintext)
    #     # decrypted_plaintext_ascii = ''.join([chr(int(decrypted_plaintext_str[i:i+8], 2)) for i in range(0, len(decrypted_plaintext_str), 8)])
    #     # print(f"Decrypted Plaintext Block {i+1}: {decrypted_plaintext_ascii}")
    #     decrypted_text.append(decrypted_plaintext)
    merged_ciphertext_hex = ''.join(list_ciphertext_hex)
    # merged_ciphertext_ascii = ''.join(list_ciphertext_ascii)
    # Menyimpan ke file
    ascii_ = []
    with open(path_cipherteks, 'w', encoding='latin-1') as file:
        for ciphertexts in list_ciphertext:
            for i in range(0, len(ciphertexts), 8):
                file.write(ciphertexts[i:i+8] + " ")
                ascii_.append(ciphertexts[i:i+8] + "")
    asciiStr = package.bin_to_asciii(ascii_)
    with open(path_cipher_hex, 'w', encoding='latin-1') as file:
        file.write(merged_ciphertext_hex)

    with open(path_cipher_ascii, 'w', encoding='latin-1') as file:
        file.write(asciiStr)

    # with open('ciphertext_grain128/decrypted_grain1281.txt', 'w', encoding='utf8') as file:
    #     for decrypted_block in decrypted_text:
    #         decrypted_block_str = ''.join(str(bit) for bit in decrypted_block)
    #         decrypted_block_ascii = ''.join(
    #             [chr(int(decrypted_block_str[i:i+8], 2)) for i in range(0, len(decrypted_block_str), 8)])
    #         file.write(decrypted_block_ascii)

    correlation = package.calculate_correlation(
        plaintext, asciiStr)
    print(f"Korelasi antara {title} dan Ciphertext:", abs(correlation))

    # Perhitungan perbedaan dipangkatkan dua
    diff_squared = package.calculate_text_difference_squared(
        plaintext, asciiStr)
    print("PSNR:", abs(diff_squared))
    plots = package.PlotHistogram()
    # Calculate histogram for plaintext
    plaintext_histogram = plots.calculate_histogram(plaintext)
    # Calculate histogram for ciphertext
    ciphertext_histogram = plots.calculate_histogram(asciiStr)

    plots.plot_ascii_frequency(plaintext, f"{title} Histogram")
    plots.plot_ascii_frequency(asciiStr, "Ciphertext Histogram")

    plt.figure(figsize=(30, 20))
    plots.histogram_lines_graph(
        plaintext_histogram, ciphertext_histogram, f"{title} vs Ciphertext Histogram")
    # Menampilkan grafik

    plt.show()

    return timer.get_duration(), abs(correlation), abs(diff_squared)


class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def get_duration(self):
        if self.start_time is not None and self.end_time is not None:
            return self.end_time - self.start_time
        else:
            return None
