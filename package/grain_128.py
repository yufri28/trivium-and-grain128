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


class Grain128:
    def __init__(self, key):
        # Inisialisasi variabel internal
        self.LFSR1 = [0] * 93
        self.LFSR2 = [0] * 84
        self.LFSR3 = [0] * 111
        self.key = key
        self.key_length = len(key)

        # Inisialisasi register LFSR dengan kunci
        for i in range(self.key_length):
            self.LFSR1[i] = int(key[i])
            self.LFSR2[i] = int(key[i])
            self.LFSR3[i] = int(key[i])

        # Inisialisasi register LFSR dengan nilai konstan
        self.LFSR1[92] = 1
        self.LFSR2[83] = 1
        self.LFSR3[110] = 1

        # Inisialisasi register LFSR dengan nilai acak
        for i in range(8 * self.key_length):
            self.keystream()

    def keystream(self):
        # Menghitung output keystream
        feedback1 = self.LFSR1[66] ^ self.LFSR1[65] ^ self.LFSR1[62] ^ self.LFSR1[57] ^ self.LFSR1[56] ^ self.LFSR1[49] ^ self.LFSR1[47] ^ self.LFSR1[46] ^ self.LFSR1[32] ^ self.LFSR1[
            30] ^ self.LFSR1[29] ^ self.LFSR1[24] ^ self.LFSR1[23] ^ self.LFSR1[21] ^ self.LFSR1[18] ^ self.LFSR1[14] ^ self.LFSR1[11] ^ self.LFSR1[6] ^ self.LFSR1[3] ^ self.LFSR1[2] ^ self.LFSR1[0]
        feedback2 = self.LFSR2[63] ^ self.LFSR2[62] ^ self.LFSR2[60] ^ self.LFSR2[57] ^ self.LFSR2[56] ^ self.LFSR2[52] ^ self.LFSR2[51] ^ self.LFSR2[38] ^ self.LFSR2[37] ^ self.LFSR2[33] ^ self.LFSR2[32] ^ self.LFSR2[29] ^ self.LFSR2[
            27] ^ self.LFSR2[24] ^ self.LFSR2[23] ^ self.LFSR2[22] ^ self.LFSR2[21] ^ self.LFSR2[19] ^ self.LFSR2[18] ^ self.LFSR2[13] ^ self.LFSR2[12] ^ self.LFSR2[10] ^ self.LFSR2[7] ^ self.LFSR2[6] ^ self.LFSR2[5] ^ self.LFSR2[3] ^ self.LFSR2[1]
        feedback3 = self.LFSR3[109] ^ self.LFSR3[108] ^ self.LFSR3[106] ^ self.LFSR3[105] ^ self.LFSR3[104] ^ self.LFSR3[103] ^ self.LFSR3[101] ^ self.LFSR3[100] ^ self.LFSR3[97] ^ self.LFSR3[96] ^ self.LFSR3[95] ^ self.LFSR3[93] ^ self.LFSR3[91] ^ self.LFSR3[89] ^ self.LFSR3[88] ^ self.LFSR3[86] ^ self.LFSR3[82] ^ self.LFSR3[78] ^ self.LFSR3[72] ^ self.LFSR3[71] ^ self.LFSR3[69] ^ self.LFSR3[68] ^ self.LFSR3[59] ^ self.LFSR3[57] ^ self.LFSR3[56] ^ self.LFSR3[54] ^ self.LFSR3[
            52] ^ self.LFSR3[50] ^ self.LFSR3[46] ^ self.LFSR3[45] ^ self.LFSR3[43] ^ self.LFSR3[40] ^ self.LFSR3[37] ^ self.LFSR3[35] ^ self.LFSR3[34] ^ self.LFSR3[33] ^ self.LFSR3[31] ^ self.LFSR3[30] ^ self.LFSR3[29] ^ self.LFSR3[24] ^ self.LFSR3[23] ^ self.LFSR3[22] ^ self.LFSR3[19] ^ self.LFSR3[18] ^ self.LFSR3[16] ^ self.LFSR3[14] ^ self.LFSR3[12] ^ self.LFSR3[9] ^ self.LFSR3[7] ^ self.LFSR3[6] ^ self.LFSR3[5] ^ self.LFSR3[4] ^ self.LFSR3[2] ^ self.LFSR3[1]

        # Shift register LFSR1
        temp = self.LFSR1[92] ^ feedback1
        self.LFSR1 = self.LFSR1[1:]
        self.LFSR1.append(temp)

        # Shift register LFSR2
        temp = self.LFSR2[83] ^ feedback2
        self.LFSR2 = self.LFSR2[1:]
        self.LFSR2.append(temp)

        # Shift register LFSR3
        temp = self.LFSR3[110] ^ feedback3
        self.LFSR3 = self.LFSR3[1:]
        self.LFSR3.append(temp)

        # Menghasilkan satu bit keystream
        return self.LFSR1[0] ^ self.LFSR2[0] ^ self.LFSR3[0]

    def text_to_bits(self, text):
        # Mengonversi string teks menjadi representasi bit
        bits = []
        for char in text:
            # Mengonversi karakter menjadi 8-bit biner
            char_bits = format(ord(char), '08b')
            bits.extend([int(bit) for bit in char_bits])
        return bits

    def bits_to_text(self, bits):
        # Mengonversi representasi bit kembali menjadi string teks
        chars = []
        for i in range(0, len(bits), 8):
            char_bits = bits[i:i+8]
            # Mengonversi 8-bit biner menjadi karakter
            char = chr(int(''.join(str(bit) for bit in char_bits), 2))
            chars.append(char)
        return ''.join(chars)

    def encrypt(self, plaintext, key):
        # Inisialisasi objek Grain-128 dengan kunci
        # grain = Grain128(key)

        # Mengonversi plaintext menjadi representasi bit
        plaintext_bits = self.text_to_bits(plaintext)

        ciphertext = ""
        # ciphertext = []

        # Mengenkripsi setiap bit plaintext menggunakan keystream
        for bit in plaintext_bits:
            keystream_bit = self.keystream()
            ciphertext_bit = bit ^ keystream_bit
            ciphertext += str(ciphertext_bit)
            # ciphertext.append(ciphertext_bit)

        return ciphertext

    # def decrypt(self, ciphertext, key):
    #     # Inisialisasi objek Grain-128 dengan kunci
    #     grain = Grain128(key)

    #     plaintext_bits = []

    #     # Mendekripsi setiap bit ciphertext menggunakan keystream
    #     for bit in ciphertext:
    #         keystream_bit = grain.keystream()
    #         plaintext_bit = bit ^ keystream_bit
    #         plaintext_bits.append(plaintext_bit)

    #     # Mengonversi representasi bit kembali menjadi string teks
    #     plaintext = grain.bits_to_text(plaintext_bits)

    #     return plaintext

    def decrypt(self, ciphertext, key):
        # self.initialize(key)
        plaintext_bits = []
        for bit in ciphertext:
            keystream_bit = self.keystream()
            plaintext_bit = int(bit) ^ keystream_bit
            plaintext_bits.append(plaintext_bit)
        return plaintext_bits

    def split_into_blocks(self, text, block_size):
        blocks = []
        num_blocks = len(text) // block_size

        for i in range(num_blocks):
            block = text[i * block_size: (i + 1) * block_size]
            blocks.append(block)

        # Mengatasi sisa teks yang kurang dari panjang satu blok
        if len(text) % block_size != 0:
            remaining = text[num_blocks * block_size:]
            blocks.append(remaining)

        return blocks

    def merge_decrypt(self, block):
        plaintext = "".join(str(block))

        return plaintext

    def biner_to_ascii_str(self, plaintext_blocks):
        ascii_string = ""
        list__chipertext = []     # List to store the ciphertext as a list of bits
        list_chiper_hex = []      # List to store the ciphertext as a hexadecimal string

        # Encrypt and print each plaintext block
        for i, block in enumerate(plaintext_blocks):
            # Encrypt the plaintext block
            ciphertext = self.encrypt(block, self.key)
            # Convert the ciphertext bits to a string
            # Mengonversi biner ke ASCII
            for j in range(0, len(ciphertext), 8):

                # Mengambil blok 8-bit dari string biner ciphertext
                block = ciphertext[j:j+8]

                # Mengonversi blok 8-bit menjadi bilangan bulat
                integer = int(block, 2)

                # Mengonversi bilangan bulat ke karakter ASCII
                # character = chr(integer)
                character = chr(integer) if integer < 255 else chr(
                    integer % 256)

                # Menyimpan karakter ke dalam string ASCII
                ascii_string += f" {character}"
        return ascii_string
