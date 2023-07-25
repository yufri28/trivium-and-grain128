import numpy as np
import math


def calculate_correlation(text1, text2):
    # Normalize the length of texts
    length = min(len(text1), len(text2))
    text1 = text1[:length]
    text2 = text2[:length]

    # Convert texts to ASCII codes
    ascii_text1 = [ord(c) for c in text1]
    ascii_text2 = [ord(c) for c in text2]

    # Calculate the mean of ASCII codes for each text
    mean_text1 = np.mean(ascii_text1)
    mean_text2 = np.mean(ascii_text2)

    # Calculate the deviations from the mean for each text
    deviations_text1 = ascii_text1 - mean_text1
    deviations_text2 = ascii_text2 - mean_text2

    # Calculate the product of deviations
    product_deviations = deviations_text1 * deviations_text2

    # Calculate the sum of squared deviations
    sum_squared_deviations_text1 = np.sum(deviations_text1 ** 2)
    sum_squared_deviations_text2 = np.sum(deviations_text2 ** 2)

    # Calculate the square root of the product of sum of squared deviations
    sqrt_product_sum_squared_deviations = np.sqrt(
        sum_squared_deviations_text1 * sum_squared_deviations_text2
    )

    # Calculate the correlation coefficient
    correlation = np.sum(product_deviations) / \
        sqrt_product_sum_squared_deviations

    return correlation


def calculate_text_difference_squared(text1, text2):
    if len(text1) != len(text2):
        raise ValueError("Texts must have equal length")
    ascii_diff_squared = [(ord(ch1) - ord(ch2)) **
                          2 for ch1, ch2 in zip(text1, text2)]
    mse = sum(ascii_diff_squared)/len(text1)
    if(mse != 0.0):
        psnr = 10 * math.log10((255**2) / mse)
    else:
        psnr = 0
    return psnr


class LCG:
    def __init__(self, kunci):
        self.kunci = kunci

    def generateKunciBaru(self, plainteks):
        while len(self.kunci) <= len(plainteks):
            x_awal = 0
            for i in range(0, len(self.kunci)):
                x_awal += (ord(self.kunci[i]) / 255)

            x1 = x_awal / len(self.kunci)

            p = 0.8  # Parameter p dalam rumus tent map

            panjangKunci = len(self.kunci)
            kuncitentmap = [0] * (panjangKunci + 1)
            x2 = [0] * (panjangKunci + 1)

            for o in range(1, panjangKunci + 1):
                if 0 <= x1 <= p:
                    x1 = x1 / p
                else:
                    x1 = (1 - x1) / (1 - p)

                # Kunci baru Tent Map
                x2[o] += (x1 * 256) % len(self.kunci) + 1
                kuncitentmap[o] += math.floor(x1 * 256)
                self.kunci += chr(kuncitentmap[o])
        return self.kunci

    def encrypt(self, plainteks):
        kunci_baru = self.generateKunciBaru(plainteks)
        print(f"Kunci Baru : {kunci_baru}")
        panjangKunci = len(kunci_baru)
        kuncitentmap = [0] * (panjangKunci + 1)
        x2 = [0] * (panjangKunci + 1)
        kuncilcg = [0] * (panjangKunci + 1)
        x4 = [0] * (panjangKunci + 1)
        x5 = [0] * (panjangKunci + 1)
        x6 = [0] * (panjangKunci + 1)
        cipher = ""

        x_awal = 0
        for i in range(0, len(kunci_baru)):
            x_awal += (ord(kunci_baru[i]) / 255)

        x1 = x_awal / len(kunci_baru)

        p = 0.8  # Parameter p dalam rumus tent map

        for o in range(1, panjangKunci + 1):
            if 0 <= x1 <= p:
                x1 = x1 / p
            else:
                x1 = (1 - x1) / (1 - p)

            x2[o] = (x1 * 256) % len(kunci_baru) + 1
            kuncitentmap[o] = math.floor(x1 * 256)

        for o in range(1, len(plainteks) + 1):
            kuncilcg[o] = kuncitentmap[math.floor(x2[o])]
            x4[o] = ord(plainteks[o - 1])
            x5[o] = x4[o]
            x6[o] = x4[o] ^ kuncilcg[o]
            cipher += chr(x6[o])

        return cipher

    def decrypt(self, cipher):
        kunci_baru = self.generateKunciBaru(cipher)
        panjangKunci = len(kunci_baru)
        kuncitentmap = [0] * (panjangKunci + 1)
        x2 = [0] * (panjangKunci + 1)
        kuncilcg = [0] * (panjangKunci + 1)
        x4 = [0] * (panjangKunci + 1)
        x5 = [0] * (panjangKunci + 1)
        decrypted = ""

        x_awal = 0
        for i in range(0, len(kunci_baru)):
            x_awal += (ord(kunci_baru[i]) / 255)

        x1 = x_awal / len(kunci_baru)

        p = 0.8  # Parameter p dalam rumus tent map

        for o in range(1, panjangKunci + 1):
            if 0 <= x1 <= p:
                x1 = x1 / p
            else:
                x1 = (1 - x1) / (1 - p)

            x2[o] = (x1 * 256) % len(kunci_baru) + 1
            kuncitentmap[o] = math.floor(x1 * 256)

        for o in range(1, len(cipher) + 1):
            kuncilcg[o] = kuncitentmap[math.floor(x2[o])]
            x4[o] = ord(cipher[o - 1])
            x5[o] = x4[o] ^ kuncilcg[o]
            decrypted += chr(x5[o])

        return decrypted
