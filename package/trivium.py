import numpy as np
import math


def bin_to_ascii(binary_string):
    decimal_value = int(binary_string, 2)
    ascii_character = chr(decimal_value)
    return ascii_character


def bin_to_asciii(binary_string):
    return ''.join([chr(int(i, 2)) for i in binary_string])


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


class Trivium:
    def __init__(self, key, iv):
        self.state = [0] * 288
        self.key_stream = []

        # Inisialisasi register dengan key dan iv
        self.init_register(key, iv)

        # Menghasilkan 1152 bit key stream
        for _ in range(1152):
            self.generate_bit()

    def init_register(self, key, iv):
        # Memasukkan key ke register
        for i in range(len(key)):
            self.state[i] = key[i]

        # Memasukkan iv ke register
        for i in range(len(iv)):
            self.state[i + 93] = iv[i]

        # Inisialisasi nilai pada bit 285, 286, dan 287
        self.state[285] = 1
        self.state[286] = 1
        self.state[287] = 1

        # Bergeser nilai pada register sebanyak 4 kali 288 bit
        for _ in range(4 * 288):
            self.generate_bit()

    def generate_bit(self):
        t1 = self.state[65] ^ self.state[92]
        t2 = self.state[161] ^ self.state[176]
        t3 = self.state[242] ^ self.state[287]

        z = t1 ^ t2 ^ t3

        t1 = t1 ^ (self.state[90] & self.state[91]) ^ self.state[170]
        t2 = t2 ^ (self.state[174] & self.state[175]) ^ self.state[263]
        t3 = t3 ^ (self.state[285] & self.state[286]) ^ self.state[68]

        # Bergeser semua bit di register ke kanan
        for i in range(287, 0, -1):
            self.state[i] = self.state[i - 1]

        self.state[0] = z

        # Menyimpan bit kunci pada key stream
        self.key_stream.append(t1 ^ t2 ^ t3)

    def encrypt(self, plaintext):
        # Mengubah teks menjadi urutan bit
        plaintext_bits = []
        for char in plaintext:
            # Mengonversi karakter menjadi urutan bit 8-bit
            bin_value = bin(ord(char))[2:].zfill(8)
            plaintext_bits.extend(map(int, bin_value))

        # Enkripsi pesan
        ciphertext = ""
        for i in range(len(plaintext_bits)):
            # Mengambil bit key stream
            key_bit = self.key_stream[i]

            # Melakukan operasi XOR pada bit plaintext dan key stream
            encrypted_bit = plaintext_bits[i] ^ key_bit

            # Mengubah bit hasil XOR menjadi karakter dan menambahkannya ke ciphertext
            ciphertext += str(encrypted_bit)

        return ciphertext

    def decrypt(self, ciphertext):
        decrypted_bits = ""
        for i in range(len(ciphertext)):
            # Mengambil bit key stream
            key_bit = self.key_stream[i]

            # Melakukan operasi XOR pada bit ciphertext dan key stream
            decrypted_bit = int(ciphertext[i]) ^ key_bit

            # Menambahkan bit hasil XOR ke decrypted_bits
            decrypted_bits += str(decrypted_bit)

        # Mengubah urutan bit menjadi teks
        decrypted_text = ""
        for j in range(0, len(decrypted_bits), 8):
            bit_chunk = decrypted_bits[j:j+8]
            char_value = int(bit_chunk, 2)
            decrypted_text += chr(char_value)

        return decrypted_text

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

    # def split_into_blocks(self, text, block_size):
    #     blocks = []
    #     num_blocks = len(text) // block_size

    #     # Mengisi sisa blok dengan bit 0
    #     if len(text) % block_size != 0:
    #         remaining = text[num_blocks * block_size:]
    #         remaining += '0' * (block_size - len(remaining))
    #         blocks.append(remaining)

    #     for i in range(num_blocks):
    #         block = text[i * block_size: (i + 1) * block_size]
    #         blocks.append(block)

    #     return blocks

    def merge_decrypt(self, block):
        plaintext = "".join(block)

        return plaintext

    # mengubah biner ke ascii dengan ascii 255
    def biner_to_ascii_str(self, plaintext_blocks):
        ascii_string = ""
        for i, block in enumerate(plaintext_blocks):
            ciphertext = self.encrypt(block)

            # Mengonversi biner ke ASCII
            for j in range(0, len(ciphertext), 8):

                # Mengambil blok 8-bit dari string biner ciphertext
                block = ciphertext[j:j+8]

                # Mengonversi blok 8-bit menjadi bilangan bulat
                integer = int(block, 2)

                # Mengonversi bilangan bulat ke karakter ASCII
                character = chr(integer) if integer < 255 else chr(
                    integer % 256)

                # Menyimpan karakter ke dalam string ASCII
                ascii_string += f" {character}"
        return ascii_string
