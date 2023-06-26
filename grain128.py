import package
import matplotlib.pyplot as plt


def plainteks_pertama(key_str):

    with open('plaintext1.txt', 'r') as file:
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

    decrypted_text = []
    for i, block in enumerate(list_ciphertext):
        decrypted_plaintext = grain128.decrypt(block, key)
        decrypted_plaintext_str = ''.join(
            str(bit) for bit in decrypted_plaintext)
        decrypted_plaintext_ascii = ''.join(
            [chr(int(decrypted_plaintext_str[i:i+8], 2)) for i in range(0, len(decrypted_plaintext_str), 8)])

        # print(f"Decrypted Plaintext Block {i+1}: {decrypted_plaintext_ascii}")
        decrypted_text.append(decrypted_plaintext)

    merged_ciphertext_hex = ''.join(list_ciphertext_hex)
    merged_ciphertext_ascii = ''.join(list_ciphertext_ascii)

    # Menyimpan ke file
    with open('ciphertext_grain128/ciphertext_grain1281.txt', 'w') as file:
        for ciphertext in list_ciphertext:
            file.write(' '.join(map(str, ciphertext)) + '\n')

    with open('ciphertext_grain128/ciphertext_grain128_hex1.txt', 'w') as file:
        file.write(merged_ciphertext_hex)

    with open('ciphertext_grain128/ciphertext_grain128_ascii1.txt', 'w', encoding='utf8') as file:
        file.write(merged_ciphertext_ascii)

    with open('ciphertext_grain128/decrypted_grain1281.txt', 'w', encoding='utf8') as file:
        for decrypted_block in decrypted_text:
            decrypted_block_str = ''.join(str(bit) for bit in decrypted_block)
            decrypted_block_ascii = ''.join(
                [chr(int(decrypted_block_str[i:i+8], 2)) for i in range(0, len(decrypted_block_str), 8)])
            file.write(decrypted_block_ascii)

    correlation = package.calculate_correlation(
        plaintext, merged_ciphertext_ascii)
    print("Korelasi antara plaintext 1 dan ciphertext:", correlation)

    # Perhitungan perbedaan dipangkatkan dua
    diff_squared = package.calculate_text_difference_squared(
        plaintext, merged_ciphertext_ascii)
    print("PSNR:", abs(diff_squared))

    plots = package.PlotHistogram()
    # plotLine = package.PlotHistogramLine()
    # Calculate histogram for plaintext
    plaintext_histogram = plots.calculate_histogram(plaintext)
    # Calculate histogram for ciphertext
    ciphertext_histogram = plots.calculate_histogram(merged_ciphertext_ascii)
    plots.plot_histogram(plaintext_histogram, "Plaintext 1 Histogram")
    plots.plot_histogram(ciphertext_histogram, "Ciphertext Histogram")
    # plots.histogram_plain_chiper(plaintext_histogram, ciphertext_histogram)

    plt.figure(figsize=(30, 20))
    plots.histogram_lines_graph(
        plaintext_histogram, ciphertext_histogram, "Plaintext 1 vs Ciphertext Histogram")
    # Menampilkan grafik

    plt.show()


def plainteks_kedua(key_str):

    with open('plaintext2.txt', 'r') as file:
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

    decrypted_text = []
    for i, block in enumerate(list_ciphertext):
        decrypted_plaintext = grain128.decrypt(block, key)
        decrypted_plaintext_str = ''.join(
            str(bit) for bit in decrypted_plaintext)
        decrypted_plaintext_ascii = ''.join(
            [chr(int(decrypted_plaintext_str[i:i+8], 2)) for i in range(0, len(decrypted_plaintext_str), 8)])

        # print(f"Decrypted Plaintext Block {i+1}: {decrypted_plaintext_ascii}")
        decrypted_text.append(decrypted_plaintext)

    merged_ciphertext_hex = ''.join(list_ciphertext_hex)
    merged_ciphertext_ascii = ''.join(list_ciphertext_ascii)

    # Menyimpan ke file
    with open('ciphertext_grain128/ciphertext_grain1282.txt', 'w') as file:
        for ciphertext in list_ciphertext:
            file.write(' '.join(map(str, ciphertext)) + '\n')

    with open('ciphertext_grain128/ciphertext_grain128_hex2.txt', 'w') as file:
        file.write(merged_ciphertext_hex)

    with open('ciphertext_grain128/ciphertext_grain128_ascii2.txt', 'w', encoding='utf8') as file:
        file.write(merged_ciphertext_ascii)

    with open('ciphertext_grain128/decrypted_grain1282.txt', 'w', encoding='utf8') as file:
        for decrypted_block in decrypted_text:
            decrypted_block_str = ''.join(str(bit) for bit in decrypted_block)
            decrypted_block_ascii = ''.join(
                [chr(int(decrypted_block_str[i:i+8], 2)) for i in range(0, len(decrypted_block_str), 8)])
            file.write(decrypted_block_ascii)

    correlation = package.calculate_correlation(
        plaintext, merged_ciphertext_ascii)
    print("Korelasi antara plaintext 2  dan ciphertext:", correlation)

    # Perhitungan perbedaan dipangkatkan dua
    diff_squared = package.calculate_text_difference_squared(
        plaintext, merged_ciphertext_ascii)
    print("PSNR:", abs(diff_squared))

    plots = package.PlotHistogram()
    # plotLine = package.PlotHistogramLine()
    # Calculate histogram for plaintext
    plaintext_histogram = plots.calculate_histogram(plaintext)
    # Calculate histogram for ciphertext
    ciphertext_histogram = plots.calculate_histogram(merged_ciphertext_ascii)
    plots.plot_histogram(plaintext_histogram, "Plaintext 2 Histogram")
    plots.plot_histogram(ciphertext_histogram, "Ciphertext Histogram")
    # plots.histogram_plain_chiper(plaintext_histogram, ciphertext_histogram)

    plt.figure(figsize=(30, 20))
    plots.histogram_lines_graph(
        plaintext_histogram, ciphertext_histogram, "Plaintext 2 vs Ciphertext Histogram")
    # Menampilkan grafik

    plt.show()


def plainteks_ketiga(key_str):

    with open('plaintext3.txt', 'r') as file:
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

    decrypted_text = []
    for i, block in enumerate(list_ciphertext):
        decrypted_plaintext = grain128.decrypt(block, key)
        decrypted_plaintext_str = ''.join(
            str(bit) for bit in decrypted_plaintext)
        decrypted_plaintext_ascii = ''.join(
            [chr(int(decrypted_plaintext_str[i:i+8], 2)) for i in range(0, len(decrypted_plaintext_str), 8)])

        # print(f"Decrypted Plaintext Block {i+1}: {decrypted_plaintext_ascii}")
        decrypted_text.append(decrypted_plaintext)

    merged_ciphertext_hex = ''.join(list_ciphertext_hex)
    merged_ciphertext_ascii = ''.join(list_ciphertext_ascii)

    # Menyimpan ke file
    with open('ciphertext_grain128/ciphertext_grain1283.txt', 'w') as file:
        for ciphertext in list_ciphertext:
            file.write(' '.join(map(str, ciphertext)) + '\n')

    with open('ciphertext_grain128/ciphertext_grain128_hex3.txt', 'w') as file:
        file.write(merged_ciphertext_hex)

    with open('ciphertext_grain128/ciphertext_grain128_ascii3.txt', 'w', encoding='utf8') as file:
        file.write(merged_ciphertext_ascii)

    with open('ciphertext_grain128/decrypted_grain1281.txt', 'w', encoding='utf8') as file:
        for decrypted_block in decrypted_text:
            decrypted_block_str = ''.join(str(bit) for bit in decrypted_block)
            decrypted_block_ascii = ''.join(
                [chr(int(decrypted_block_str[i:i+8], 2)) for i in range(0, len(decrypted_block_str), 8)])
            file.write(decrypted_block_ascii)

    correlation = package.calculate_correlation(
        plaintext, merged_ciphertext_ascii)
    print("Korelasi antara plaintext 3 dan ciphertext:", correlation)

    # Perhitungan perbedaan dipangkatkan dua
    diff_squared = package.calculate_text_difference_squared(
        plaintext, merged_ciphertext_ascii)
    print("PSNR:", abs(diff_squared))

    plots = package.PlotHistogram()
    # plotLine = package.PlotHistogramLine()
    # Calculate histogram for plaintext
    plaintext_histogram = plots.calculate_histogram(plaintext)
    # Calculate histogram for ciphertext
    ciphertext_histogram = plots.calculate_histogram(merged_ciphertext_ascii)
    plots.plot_histogram(plaintext_histogram, "Plaintext 3 Histogram")
    plots.plot_histogram(ciphertext_histogram, "Ciphertext Histogram")
    # plots.histogram_plain_chiper(plaintext_histogram, ciphertext_histogram)

    plt.figure(figsize=(30, 20))
    plots.histogram_lines_graph(
        plaintext_histogram, ciphertext_histogram, "Plaintext 3 vs Ciphertext Histogram")
    # Menampilkan grafik

    plt.show()


def plainteks_keempat(key_str):

    with open('plaintext4.txt', 'r') as file:
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

    decrypted_text = []
    for i, block in enumerate(list_ciphertext):
        decrypted_plaintext = grain128.decrypt(block, key)
        decrypted_plaintext_str = ''.join(
            str(bit) for bit in decrypted_plaintext)
        decrypted_plaintext_ascii = ''.join(
            [chr(int(decrypted_plaintext_str[i:i+8], 2)) for i in range(0, len(decrypted_plaintext_str), 8)])

        # print(f"Decrypted Plaintext Block {i+1}: {decrypted_plaintext_ascii}")
        decrypted_text.append(decrypted_plaintext)

    merged_ciphertext_hex = ''.join(list_ciphertext_hex)
    merged_ciphertext_ascii = ''.join(list_ciphertext_ascii)

    # Menyimpan ke file
    with open('ciphertext_grain128/ciphertext_grain1284.txt', 'w') as file:
        for ciphertext in list_ciphertext:
            file.write(' '.join(map(str, ciphertext)) + '\n')

    with open('ciphertext_grain128/ciphertext_grain128_hex4.txt', 'w') as file:
        file.write(merged_ciphertext_hex)

    with open('ciphertext_grain128/ciphertext_grain128_ascii4.txt', 'w', encoding='utf8') as file:
        file.write(merged_ciphertext_ascii)

    with open('ciphertext_grain128/decrypted_grain1284.txt', 'w', encoding='utf8') as file:
        for decrypted_block in decrypted_text:
            decrypted_block_str = ''.join(str(bit) for bit in decrypted_block)
            decrypted_block_ascii = ''.join(
                [chr(int(decrypted_block_str[i:i+8], 2)) for i in range(0, len(decrypted_block_str), 8)])
            file.write(decrypted_block_ascii)

    correlation = package.calculate_correlation(
        plaintext, merged_ciphertext_ascii)
    print("Korelasi antara plaintext 4 dan ciphertext:", correlation)

    # Perhitungan perbedaan dipangkatkan dua
    diff_squared = package.calculate_text_difference_squared(
        plaintext, merged_ciphertext_ascii)
    print("PSNR:", abs(diff_squared))

    plots = package.PlotHistogram()
    # plotLine = package.PlotHistogramLine()
    # Calculate histogram for plaintext
    plaintext_histogram = plots.calculate_histogram(plaintext)
    # Calculate histogram for ciphertext
    ciphertext_histogram = plots.calculate_histogram(merged_ciphertext_ascii)
    plots.plot_histogram(plaintext_histogram, "Plaintext 4 Histogram")
    plots.plot_histogram(ciphertext_histogram, "Ciphertext Histogram")
    # plots.histogram_plain_chiper(plaintext_histogram, ciphertext_histogram)

    plt.figure(figsize=(30, 20))
    plots.histogram_lines_graph(
        plaintext_histogram, ciphertext_histogram, "Plaintext 4 vs Ciphertext Histogram")
    # Menampilkan grafik

    plt.show()


def plainteks_kelima(key_str):

    with open('plaintext5.txt', 'r') as file:
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

    decrypted_text = []
    for i, block in enumerate(list_ciphertext):
        decrypted_plaintext = grain128.decrypt(block, key)
        decrypted_plaintext_str = ''.join(
            str(bit) for bit in decrypted_plaintext)
        decrypted_plaintext_ascii = ''.join(
            [chr(int(decrypted_plaintext_str[i:i+8], 2)) for i in range(0, len(decrypted_plaintext_str), 8)])

        # print(f"Decrypted Plaintext Block {i+1}: {decrypted_plaintext_ascii}")
        decrypted_text.append(decrypted_plaintext)

    merged_ciphertext_hex = ''.join(list_ciphertext_hex)
    merged_ciphertext_ascii = ''.join(list_ciphertext_ascii)

    # Menyimpan ke file
    with open('ciphertext_grain128/ciphertext_grain1285.txt', 'w') as file:
        for ciphertext in list_ciphertext:
            file.write(' '.join(map(str, ciphertext)) + '\n')

    with open('ciphertext_grain128/ciphertext_grain128_hex5.txt', 'w') as file:
        file.write(merged_ciphertext_hex)

    with open('ciphertext_grain128/ciphertext_grain128_ascii5.txt', 'w', encoding='utf8') as file:
        file.write(merged_ciphertext_ascii)

    with open('ciphertext_grain128/decrypted_grain1285.txt', 'w', encoding='utf8') as file:
        for decrypted_block in decrypted_text:
            decrypted_block_str = ''.join(str(bit) for bit in decrypted_block)
            decrypted_block_ascii = ''.join(
                [chr(int(decrypted_block_str[i:i+8], 2)) for i in range(0, len(decrypted_block_str), 8)])
            file.write(decrypted_block_ascii)

    correlation = package.calculate_correlation(
        plaintext, merged_ciphertext_ascii)
    print("Korelasi antara plaintext 5 dan ciphertext:", correlation)

    # Perhitungan perbedaan dipangkatkan dua
    diff_squared = package.calculate_text_difference_squared(
        plaintext, merged_ciphertext_ascii)
    print("PSNR:", abs(diff_squared))

    plots = package.PlotHistogram()
    # plotLine = package.PlotHistogramLine()
    # Calculate histogram for plaintext
    plaintext_histogram = plots.calculate_histogram(plaintext)
    # Calculate histogram for ciphertext
    ciphertext_histogram = plots.calculate_histogram(merged_ciphertext_ascii)
    plots.plot_histogram(plaintext_histogram, "Plaintext 5 Histogram")
    plots.plot_histogram(ciphertext_histogram, "Ciphertext Histogram")
    # plots.histogram_plain_chiper(plaintext_histogram, ciphertext_histogram)

    plt.figure(figsize=(30, 20))
    plots.histogram_lines_graph(
        plaintext_histogram, ciphertext_histogram, "Plaintext 5 vs Ciphertext Histogram")
    # Menampilkan grafik

    plt.show()


key_str = "adrian"
plainteks_pertama(key_str)
