from collections import deque
from itertools import repeat
import numpy as np
import math

# Convert strings of hex to strings of bytes and back, little-endian style
_allbytes = dict([("%02X" % i, i) for i in range(256)])


def hex_to_bytes(s):
    return [_allbytes[s[i:i+2].upper()] for i in range(0, len(s), 2)]


def hex_to_bits(s):
    return [(b >> i) & 1 for b in hex_to_bytes(s)
            for i in range(8)]


def bits_to_hex(b):
    return "".join(["%02X" % sum([b[i + j] << j for j in range(8)])
                    for i in range(0, len(b), 8)])


def str_to_bits(s):
    return [int(bit) for char in s for bit in bin(ord(char))[2:].zfill(8)]


def bin_to_ascii(binary_string):
    decimal_value = int(binary_string, 2)
    ascii_character = chr(decimal_value)
    return ascii_character


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


def bit_to_ascii(bit_string):
    """Converts a string of bits to ASCII text."""
    bits = [int(bit) for bit in bit_string]
    ascii_text = ""
    for i in range(0, len(bits), 8):
        byte_bits = bits[i:i+8]
        byte = sum(bit << (7 - j) for j, bit in enumerate(byte_bits))
        ascii_text += chr(byte)
    return ascii_text


class Trivium:
    def __init__(self, key, iv):
        """in the beginning we need to transform the key as well as the IV.
        Afterwards we initialize the state."""
        self.state = None
        self.counter = 0
        self.key = key
        self.iv = iv

        # Initialize state
        # len 93
        init_list = list(map(int, list(self.key)))
        init_list += list(repeat(0, 13))
        # len 84
        init_list += list(map(int, list(self.iv)))
        init_list += list(repeat(0, 4))
        # len 111
        init_list += list(repeat(0, 108))
        init_list += list([1, 1, 1])
        self.state = deque(init_list)

        # Do 4 full cycles, drop output
        for i in range(4*288):
            self._gen_keystream()

    def encrypt(self, message):
        next_key_bit = self.keystream().__next__
        cipher = deque([])
        for byte in bytearray(message, "utf8"):
            # Key for each byte
            key = 0
            for i in range(0, 8):
                k = next_key_bit()
                key = key | (k << i)

            c = [int(i, 2) for i in bin(byte ^ key)[2:].zfill(8)]

            # Little Endian
            cipher.extendleft(c[4:])
            cipher.extendleft(c[:4])

        return list(cipher)

    def decrypt(self, cipher):
        next_key_bit = self.keystream().__next__

        cipher = deque(cipher)
        plain = deque([])

        for i in range(0, int((len(cipher) / 8))):
            temp = []
            for j in range(0, 8):
                temp.append(cipher.pop())

            # cipher
            c_list = []
            c_list[:4] = temp[4:]
            c_list[4:] = temp[:4]
            c = int("".join(str(i) for i in c_list), 2)

            # key
            key = 0
            for j in range(0, 8):
                k = next_key_bit()
                key = key | (k << j)

            # plain text
            plain.extendleft([c ^ key])

        return ''.join(chr(i) for i in list(plain)[::-1])

    def keystream(self):
        """output keystream
        only use this when you know what you are doing!!"""
        while self.counter < 2**64:
            self.counter += 1
            yield self._gen_keystream()

    def _gen_keystream(self):
        """this method generates triviums keystream"""

        t_1 = self.state[65] ^ self.state[92]
        t_2 = self.state[161] ^ self.state[176]
        t_3 = self.state[242] ^ self.state[287]

        out = t_1 ^ t_2 ^ t_3

        a_1 = self.state[90] & self.state[91]
        a_2 = self.state[174] & self.state[175]
        a_3 = self.state[285] & self.state[286]

        s_1 = a_1 ^ self.state[170] ^ t_1
        s_2 = a_2 ^ self.state[263] ^ t_2
        s_3 = a_3 ^ self.state[68] ^ t_3

        self.state.rotate(1)

        self.state[0] = s_3
        self.state[93] = s_1
        self.state[177] = s_2

        return out

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
