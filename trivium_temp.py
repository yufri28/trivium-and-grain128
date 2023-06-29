import matplotlib.pyplot as plt
import package


def plainteks_pertama(key_str, iv_str):
    toBitList = package.ToBitList()
    key_bits = toBitList.str_to_bit_list(key_str)
    iv_bits = toBitList.str_to_bit_list(iv_str)
    trivium = package.Trivium(key_bits, iv_bits)

    # Pesan yang akan dienkripsi
    # plaintext = "saya"
    with open('plaintext1.txt', 'r') as file:
        plaintext = file.read()

    # inisialisasi ukuran setiap block dengan max 80 karakter atau bit
    block_size = 80
    # print(plaintext)
    plaintext_blocks = trivium.split_into_blocks(plaintext, block_size)
    binerToAsciiStr = trivium.biner_to_ascii_str(plaintext_blocks)

    list_ciphertext = []
    list_ciphertext_ascii = []

    # Cetak blok-blok hasil pembagian
    for i, block in enumerate(plaintext_blocks):
        ciphertext = trivium.encrypt(block)
        # Konversi bilangan biner ke ASCII
        ciphertext_ascii = ''.join([package.bin_to_ascii(ciphertext[i:i+8])
                                    for i in range(0, len(ciphertext), 8)])

        # print(f"Ciphertext Blok {i+1}: {ciphertext_ascii}")
        list_ciphertext.append(ciphertext)
        list_ciphertext_ascii.append(ciphertext_ascii)

    # Menggabungkan semua blok ciphertext menjadi satu string tunggal
    merged_ciphertext_ascii = ''.join(list_ciphertext_ascii)
    # Memecah ciphertext menjadi blok 8 bit
    for ciphertext1 in list_ciphertext:
        blocks = [ciphertext1[i:i+8] for i in range(0, len(ciphertext1), 8)]
        # Menyimpan ke file plaintext dan ciphertext
    ascii_ = []
    with open('ciphertext_trivium/ciphertext1.txt', 'w') as file:
        for ciphertexts in list_ciphertext:
            for i in range(0, len(ciphertexts), 8):
                file.write(ciphertexts[i:i+8] + " ")
                ascii_.append(ciphertexts[i:i+8] + "")

    # with open('ciphertext_trivium/ciphertext1.txt', 'r') as file:
    #     for add in file.read():
    #         ascii_.append(add)

    asciiStr = package.bin_to_asciii(ascii_)

    correlation = package.calculate_correlation(
        plaintext, asciiStr)
    print("Korelasi antara plaintext 1 dan ciphertext:", correlation)

    # Perhitungan perbedaan dipangkatkan dua
    diff_squared = package.calculate_text_difference_squared(
        plaintext, asciiStr)
    print("PSNR:", abs(diff_squared))

    # Menyimpan ke file plaintext dan ciphertext
    # with open('ciphertext_trivium/ciphertext1.txt', 'w') as file:
    #     for ciphertext in blocks:
    #         file.write(ciphertext + "\s")

    with open('ciphertext_trivium/ciphertext_ascii1.txt', 'w', encoding='utf8') as file:
        file.write(asciiStr)

    plots = package.PlotHistogram()
    # plotLine = package.PlotHistogramLine()
    # Calculate histogram for plaintext
    plaintext_histogram = plots.calculate_histogram(plaintext)
    # Calculate histogram for ciphertext
    ciphertext_histogram = plots.calculate_histogram(asciiStr)
    # plots.plot_histogram(plaintext_histogram, "Plaintext 1 Histogram")
    # plots.plot_histogram(ciphertext_histogram, "Ciphertext Histogram")
    # plots.histogram_plain_chiper(plaintext_histogram, ciphertext_histogram)
    plots.plot_ascii_frequency(plaintext, "Plaintext 1 Histogram")
    plots.plot_ascii_frequency(asciiStr, "Ciphertext Histogram")
    plots.histogram_lines_graph(
        plaintext_histogram, ciphertext_histogram, "Plaintext 1 vs Ciphertext Histogram")
    # Menampilkan grafik
    plt.show()


def plainteks_kedua(key_str, iv_str):
    toBitList = package.ToBitList()

    key_bits = toBitList.str_to_bit_list(key_str)
    iv_bits = toBitList.str_to_bit_list(iv_str)

    trivium = package.Trivium(key_bits, iv_bits)

    # Pesan yang akan dienkripsi
    # plaintext = "saya"
    with open('plaintext2.txt', 'r') as file:
        plaintext = file.read()

    # inisialisasi ukuran setiap block dengan max 80 karakter atau bit
    block_size = 80
    # print(plaintext)
    plaintext_blocks = trivium.split_into_blocks(plaintext, block_size)

    binerToAsciiStr = trivium.biner_to_ascii_str(plaintext_blocks)

    list_ciphertext = []
    list_ciphertext_ascii = []

    # Cetak blok-blok hasil pembagian
    for i, block in enumerate(plaintext_blocks):
        ciphertext = trivium.encrypt(block)
        # Konversi bilangan biner ke ASCII
        ciphertext_ascii = ''.join([package.bin_to_ascii(ciphertext[i:i+8])
                                    for i in range(0, len(ciphertext), 8)])

        # print(f"Ciphertext Blok {i+1}: {ciphertext_ascii}")
        list_ciphertext.append(ciphertext)
        list_ciphertext_ascii.append(ciphertext_ascii)

    # Menggabungkan semua blok ciphertext menjadi satu string tunggal
    merged_ciphertext_ascii2 = ''.join(list_ciphertext_ascii)
    # Memecah ciphertext menjadi blok 8 bit
    for ciphertext1 in list_ciphertext:
        blocks = [ciphertext1[i:i+8] for i in range(0, len(ciphertext1), 8)]

    correlation = package.calculate_correlation(
        plaintext, merged_ciphertext_ascii2)
    print("Korelasi antara plaintext 2 dan ciphertext:", correlation)

    # Perhitungan perbedaan dipangkatkan dua
    diff_squared = package.calculate_text_difference_squared(
        plaintext, merged_ciphertext_ascii2)
    print("PSNR:", abs(diff_squared))
    # Menyimpan ke file plaintext dan ciphertext
    with open('ciphertext_trivium/ciphertext2.txt', 'w') as file:
        for ciphertext in list_ciphertext:
            file.write(ciphertext + '\n')

    with open('ciphertext_trivium/ciphertext_ascii2.txt', 'w', encoding='utf8') as file:
        file.write(merged_ciphertext_ascii2)

    plots = package.PlotHistogram()
    # plotLine = package.PlotHistogramLine()
    # Calculate histogram for plaintext
    plaintext_histogram = plots.calculate_histogram(plaintext)
    # Calculate histogram for ciphertext
    ciphertext_histogram = plots.calculate_histogram(merged_ciphertext_ascii2)
    # plots.plot_histogram(plaintext_histogram, "Plaintext 2 Histogram")
    # plots.plot_histogram(ciphertext_histogram, "Ciphertext Histogram")
    # plots.histogram_plain_chiper(plaintext_histogram, ciphertext_histogram)
    plots.plot_ascii_frequency(plaintext, "Plaintext 2 Histogram")
    plots.plot_ascii_frequency(
        merged_ciphertext_ascii2, "Ciphertext Histogram")

    plots.histogram_lines_graph(
        plaintext_histogram, ciphertext_histogram, "Plaintext 2 vs Ciphertext Histogram")
    # Menampilkan grafik
    plt.show()


def plainteks_ketiga(key_str, iv_str):
    toBitList = package.ToBitList()

    key_bits = toBitList.str_to_bit_list(key_str)
    iv_bits = toBitList.str_to_bit_list(iv_str)

    trivium = package.Trivium(key_bits, iv_bits)

    # Pesan yang akan dienkripsi
    # plaintext = "saya"
    with open('plaintext3.txt', 'r') as file:
        plaintext = file.read()

    # inisialisasi ukuran setiap block dengan max 80 karakter atau bit
    block_size = 80
    # print(plaintext)
    plaintext_blocks = trivium.split_into_blocks(plaintext, block_size)

    binerToAsciiStr = trivium.biner_to_ascii_str(plaintext_blocks)

    list_ciphertext = []
    list_ciphertext_ascii = []

    # Cetak blok-blok hasil pembagian
    for i, block in enumerate(plaintext_blocks):
        ciphertext = trivium.encrypt(block)
        # Konversi bilangan biner ke ASCII
        ciphertext_ascii = ''.join([package.bin_to_ascii(ciphertext[i:i+8])
                                    for i in range(0, len(ciphertext), 8)])

        # print(f"Ciphertext Blok {i+1}: {ciphertext_ascii}")
        list_ciphertext.append(ciphertext)
        list_ciphertext_ascii.append(ciphertext_ascii)

    # Menggabungkan semua blok ciphertext menjadi satu string tunggal
    merged_ciphertext_ascii3 = ''.join(list_ciphertext_ascii)
    # Memecah ciphertext menjadi blok 8 bit
    for ciphertext1 in list_ciphertext:
        blocks = [ciphertext1[i:i+8] for i in range(0, len(ciphertext1), 8)]

    correlation = package.calculate_correlation(
        plaintext, merged_ciphertext_ascii3)
    print("Korelasi antara plaintext 3 dan ciphertext:", correlation)

    # Perhitungan perbedaan dipangkatkan dua
    diff_squared = package.calculate_text_difference_squared(
        plaintext, merged_ciphertext_ascii3)
    print("PSNR:", abs(diff_squared))
    # Menyimpan ke file plaintext dan ciphertext
    with open('ciphertext_trivium/ciphertext3.txt', 'w') as file:
        for ciphertext in list_ciphertext:
            file.write(ciphertext + '\n')

    with open('ciphertext_trivium/ciphertext_ascii3.txt', 'w', encoding='utf8') as file:
        file.write(merged_ciphertext_ascii3)

    plots = package.PlotHistogram()
    # plotLine = package.PlotHistogramLine()
    # Calculate histogram for plaintext
    plaintext_histogram = plots.calculate_histogram(plaintext)
    # Calculate histogram for ciphertext
    ciphertext_histogram = plots.calculate_histogram(merged_ciphertext_ascii3)
    # plots.plot_histogram(plaintext_histogram, "Plaintext 3 Histogram")
    # plots.plot_histogram(ciphertext_histogram, "Ciphertext Histogram")
    # plots.histogram_plain_chiper(plaintext_histogram, ciphertext_histogram)
    plots.plot_ascii_frequency(plaintext, "Plaintext 3 Histogram")
    plots.plot_ascii_frequency(
        merged_ciphertext_ascii3, "Ciphertext Histogram")

    plots.histogram_lines_graph(
        plaintext_histogram, ciphertext_histogram, "Plaintext 3 vs Ciphertext Histogram")
    # Menampilkan grafik
    plt.show()


def plainteks_keempat(key_str, iv_str):
    toBitList = package.ToBitList()

    key_bits = toBitList.str_to_bit_list(key_str)
    iv_bits = toBitList.str_to_bit_list(iv_str)

    trivium = package.Trivium(key_bits, iv_bits)

    # Pesan yang akan dienkripsi
    # plaintext = "saya"
    with open('plaintext4.txt', 'r') as file:
        plaintext = file.read()

    # inisialisasi ukuran setiap block dengan max 80 karakter atau bit
    block_size = 80
    # print(plaintext)
    plaintext_blocks = trivium.split_into_blocks(plaintext, block_size)

    binerToAsciiStr = trivium.biner_to_ascii_str(plaintext_blocks)

    list_ciphertext = []
    list_ciphertext_ascii = []

    # Cetak blok-blok hasil pembagian
    for i, block in enumerate(plaintext_blocks):
        ciphertext = trivium.encrypt(block)
        # Konversi bilangan biner ke ASCII
        ciphertext_ascii = ''.join([package.bin_to_ascii(ciphertext[i:i+8])
                                    for i in range(0, len(ciphertext), 8)])

        # print(f"Ciphertext Blok {i+1}: {ciphertext_ascii}")
        list_ciphertext.append(ciphertext)
        list_ciphertext_ascii.append(ciphertext_ascii)

    # Menggabungkan semua blok ciphertext menjadi satu string tunggal
    merged_ciphertext_ascii4 = ''.join(list_ciphertext_ascii)
    # Memecah ciphertext menjadi blok 8 bit
    for ciphertext1 in list_ciphertext:
        blocks = [ciphertext1[i:i+8] for i in range(0, len(ciphertext1), 8)]

    correlation = package.calculate_correlation(
        plaintext, merged_ciphertext_ascii4)
    print("Korelasi antara plaintext 4 dan ciphertext:", correlation)

    # Perhitungan perbedaan dipangkatkan dua
    diff_squared = package.calculate_text_difference_squared(
        plaintext, merged_ciphertext_ascii4)
    print("PSNR:", abs(diff_squared))
    # Menyimpan ke file plaintext dan ciphertext
    with open('ciphertext_trivium/ciphertext4.txt', 'w') as file:
        for ciphertext in list_ciphertext:
            file.write(ciphertext + '\n')

    with open('ciphertext_trivium/ciphertext_ascii4.txt', 'w', encoding='utf8') as file:
        file.write(merged_ciphertext_ascii4)

    plots = package.PlotHistogram()
    # plotLine = package.PlotHistogramLine()
    # Calculate histogram for plaintext
    plaintext_histogram = plots.calculate_histogram(plaintext)
    # Calculate histogram for ciphertext
    ciphertext_histogram = plots.calculate_histogram(merged_ciphertext_ascii4)
    # plots.plot_histogram(plaintext_histogram, "Plaintext 4 Histogram")
    # plots.plot_histogram(ciphertext_histogram, "Ciphertext Histogram")
    # plots.histogram_plain_chiper(plaintext_histogram, ciphertext_histogram)
    plots.plot_ascii_frequency(plaintext, "Plaintext 4 Histogram")
    plots.plot_ascii_frequency(
        merged_ciphertext_ascii4, "Ciphertext Histogram")
    plots.histogram_lines_graph(
        plaintext_histogram, ciphertext_histogram, "Plaintext 4 vs Ciphertext Histogram")
    # Menampilkan grafik
    plt.show()


def plainteks_kelima(key_str, iv_str):
    toBitList = package.ToBitList()

    key_bits = toBitList.str_to_bit_list(key_str)
    iv_bits = toBitList.str_to_bit_list(iv_str)

    trivium = package.Trivium(key_bits, iv_bits)

    # Pesan yang akan dienkripsi
    # plaintext = "saya"
    with open('plaintext5.txt', 'r') as file:
        plaintext = file.read()

    # inisialisasi ukuran setiap block dengan max 80 karakter atau bit
    block_size = 80
    # print(plaintext)
    plaintext_blocks = trivium.split_into_blocks(plaintext, block_size)

    binerToAsciiStr = trivium.biner_to_ascii_str(plaintext_blocks)

    list_ciphertext = []
    list_ciphertext_ascii = []

    # Cetak blok-blok hasil pembagian
    for i, block in enumerate(plaintext_blocks):
        ciphertext = trivium.encrypt(block)
        # Konversi bilangan biner ke ASCII
        ciphertext_ascii = ''.join([package.bin_to_ascii(ciphertext[i:i+8])
                                    for i in range(0, len(ciphertext), 8)])

        # print(f"Ciphertext Blok {i+1}: {ciphertext_ascii}")
        list_ciphertext.append(ciphertext)
        list_ciphertext_ascii.append(ciphertext_ascii)

    # Menggabungkan semua blok ciphertext menjadi satu string tunggal
    merged_ciphertext_ascii5 = ''.join(list_ciphertext_ascii)
    # Memecah ciphertext menjadi blok 8 bit
    for ciphertext1 in list_ciphertext:
        blocks = [ciphertext1[i:i+8] for i in range(0, len(ciphertext1), 8)]

    correlation = package.calculate_correlation(
        plaintext, merged_ciphertext_ascii5)
    print("Korelasi antara plaintext 5 dan ciphertext:", correlation)

    # Perhitungan perbedaan dipangkatkan dua
    diff_squared = package.calculate_text_difference_squared(
        plaintext, merged_ciphertext_ascii5)
    print("PSNR:", abs(diff_squared))
    # Menyimpan ke file plaintext dan ciphertext
    with open('ciphertext_trivium/ciphertext5.txt', 'w') as file:
        for ciphertext in list_ciphertext:
            file.write(ciphertext + '\n')

    with open('ciphertext_trivium/ciphertext_ascii5.txt', 'w', encoding='utf8') as file:
        file.write(merged_ciphertext_ascii5)

    plots = package.PlotHistogram()
    # plotLine = package.PlotHistogramLine()
    # Calculate histogram for plaintext
    plaintext_histogram = plots.calculate_histogram(plaintext)
    # Calculate histogram for ciphertext
    ciphertext_histogram = plots.calculate_histogram(merged_ciphertext_ascii5)
    # plots.plot_histogram(plaintext_histogram, "Plaintext 5 Histogram")
    # plots.plot_histogram(ciphertext_histogram, "Ciphertext Histogram")
    # plots.histogram_plain_chiper(plaintext_histogram, ciphertext_histogram)
    plots.plot_ascii_frequency(plaintext, "Plaintext 5 Histogram")
    plots.plot_ascii_frequency(
        merged_ciphertext_ascii5, "Ciphertext Histogram")

    plots.histogram_lines_graph(
        plaintext_histogram, ciphertext_histogram, "Plaintext 5 vs Ciphertext Histogram")
    # Menampilkan grafik
    plt.show()
