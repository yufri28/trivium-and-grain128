import matplotlib.pyplot as plt
import package
import time


def visualize_text_trivium(key_str, iv_str, title, path_plainteks, path_cipherteks, path_cipher_ascii):
    toBitList = package.ToBitList()
    key_bits = toBitList.str_to_bit_list(key_str)
    iv_bits = toBitList.str_to_bit_list(iv_str)
    trivium = package.Trivium(key_bits, iv_bits)
    timer = Timer()

    with open(path_plainteks, 'r') as file:
        plaintext = file.read()

    block_size = 80
    plaintext_blocks = trivium.split_into_blocks(plaintext, block_size)
    binerToAsciiStr = trivium.biner_to_ascii_str(plaintext_blocks)

    list_ciphertext = []
    list_ciphertext_ascii = []
    timer.start()
    for i, block in enumerate(plaintext_blocks):
        ciphertext = trivium.encrypt(block)
    timer.stop()

    print(f"Durasi waktu eksekusi {title}:" +
          " {:.9f} detik".format(timer.get_duration()))

    for i, block in enumerate(plaintext_blocks):
        ciphertext = trivium.encrypt(block)
        ciphertext_ascii = ''.join([package.bin_to_ascii(ciphertext[i:i+8])
                                    for i in range(0, len(ciphertext), 8)])

        list_ciphertext.append(ciphertext)
        list_ciphertext_ascii.append(ciphertext_ascii)
    # merged_ciphertext_ascii = ''.join(list_ciphertext_ascii)

    ascii_ = []
    with open(path_cipherteks, 'w') as file:
        for ciphertexts in list_ciphertext:
            for i in range(0, len(ciphertexts), 8):
                file.write(ciphertexts[i:i+8] + " ")
                ascii_.append(ciphertexts[i:i+8] + "")

    asciiStr = package.bin_to_asciii(ascii_)

    correlation = package.calculate_correlation(
        plaintext, asciiStr)
    print(f"Korelasi antara {title} dan Ciphertext:", abs(correlation))

    diff_squared = package.calculate_text_difference_squared(
        plaintext, asciiStr)
    print("PSNR:", abs(diff_squared))

    with open(path_cipher_ascii, 'w', encoding='utf8') as file:
        file.write(asciiStr)

    plots = package.PlotHistogram()
    plaintext_histogram = plots.calculate_histogram(plaintext)
    ciphertext_histogram = plots.calculate_histogram(asciiStr)
    plots.plot_ascii_frequency(plaintext, f"{title} Histogram")
    plots.plot_ascii_frequency(asciiStr, "Ciphertext Histogram")
    plots.histogram_lines_graph(
        plaintext_histogram, ciphertext_histogram, f"{title} vs Ciphertext Histogram")
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
