class ToBitList:
    def str_to_bit_list(self, text):
        bits = ''.join(format(ord(c), '08b') for c in text)
        return [int(bit) for bit in bits]
