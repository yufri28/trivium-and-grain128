import matplotlib.pyplot as plt
import package
import time


def visualize_text_lcg(key, title, path_plainteks, path_cipher_ascii):

    lcg = package.LCG(key)
    timer = Timer()

    with open(path_plainteks, 'r') as file:
        plainteks = file.read()

    timer.start()
    cipher = lcg.encrypt(plainteks)
    timer.stop()
    decrypt = lcg.decrypt(cipher)
    print(f"Dekripsi : {decrypt}")
    print(f"Durasi waktu eksekusi {title}:" +
          " {:.9f} detik".format(timer.get_duration()))

    # decrypted = lcg.decrypt(cipher, key)
    # print("=============================================================")
    # print("=================== Enkrip dan Dekrip =======================")
    # print("=============================================================")
    # print(f"Plainteks: {len(plainteks)} : ", plainteks)
    # print(f"Cipherteks: {len(cipher)} : ", cipher)
    # print(f"Dekripsi: {len(decrypted)} : ", decrypted)

    correlation = package.calculate_correlation(
        plainteks, cipher)
    print(f"Korelasi antara {title} dan Ciphertext:", abs(correlation))

    diff_squared = package.calculate_text_difference_squared(
        plainteks, cipher)
    print("PSNR:", abs(diff_squared))

    with open(path_cipher_ascii, 'w', encoding='utf8') as file:
        file.write(cipher)

    plots = package.PlotHistogram()
    plaintext_histogram = plots.calculate_histogram(plainteks)
    ciphertext_histogram = plots.calculate_histogram(cipher)
    plots.plot_ascii_frequency(plainteks, f"{title} Histogram")
    plots.plot_ascii_frequency(cipher, "Ciphertext Histogram")
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
