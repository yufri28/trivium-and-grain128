import package
import matplotlib.pyplot as plt


def visualize_text_ibu(title, path_plainteks, path_cipherteks):

    with open(path_plainteks, 'r') as file:
        plaintext = file.read()

    with open(path_cipherteks, 'r', encoding='utf8') as file:
        ciphertext = file.read()

    correlation = package.calculate_correlation(
        plaintext, ciphertext)
    print(f"Korelasi antara {title} dan Ciphertext:", abs(correlation))
    # Perhitungan perbedaan dipangkatkan dua
    print(f"len plain : {len(plaintext)}")
    print(f"len ciph : {len(ciphertext)}")
    diff_squared = package.calculate_text_difference_squared(
        plaintext, ciphertext)
    print("PSNR:", abs(diff_squared))
    plots = package.PlotHistogram()
    # Calculate histogram for plaintext
    plaintext_histogram = plots.calculate_histogram(plaintext)
    # Calculate histogram for ciphertext
    ciphertext_histogram = plots.calculate_histogram(ciphertext)

    plots.plot_ascii_frequency(plaintext, f"{title} Histogram")
    plots.plot_ascii_frequency(ciphertext, "Ciphertext Histogram")

    plt.figure(figsize=(30, 20))
    plots.histogram_lines_graph(
        plaintext_histogram, ciphertext_histogram, f"{title} vs Ciphertext Histogram")
    # Menampilkan grafik

    plt.show()
