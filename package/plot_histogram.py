from collections import defaultdict
import matplotlib.pyplot as plt
from collections import Counter


class PlotHistogram:
    def calculate_histogram(self, data):
        histogram = defaultdict(int)
        # total = len(data)
        for item in data:
            histogram[item] += 1
        # for key in histogram:
        #     histogram[key] /= total
        return histogram

    def plot_histogram(self, histogram, title):
        keys = histogram.keys()
        values = histogram.values()
        plt.figure(figsize=(30, 10))
        plt.bar(keys, values)
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.title(title)
        plt.show()

    def histogram_plain_chiper(self, plaintext_histogram, ciphertext_histogram):
        # Plot histograms
        plt.figure(figsize=(10, 5))
        # Plot plaintext histogram
        plt.subplot(1, 2, 1)
        plt.bar(plaintext_histogram.keys(), plaintext_histogram.values())
        plt.xlabel("Plaintext Characters")
        plt.ylabel("Frequency")
        plt.title("Plaintext Histogram")
        # Plot ciphertext histogram
        plt.subplot(1, 2, 2)
        plt.bar(ciphertext_histogram.keys(), ciphertext_histogram.values())
        plt.xlabel("Ciphertext Characters")
        plt.ylabel("Frequency")
        plt.title("Ciphertext Histogram")
        # Adjust spacing between subplots
        plt.tight_layout()
        # Show the plot
        plt.show()

    def plot_histogram_line(self, data1, data2, title):
        keys = set(data1.keys()).union(set(data2.keys()))
        values = range(len(keys))
        plt.plot(values, [data1.get(key, 0)
                 for key in keys], 'b-', label='Plaintext')
        plt.plot(values, [data2.get(key, 0)
                 for key in keys], 'r-', label='Ciphertext')
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.title(title)
        plt.xlabel("Character")
        plt.ylabel("Frequency")
        plt.xticks(values, keys)
        plt.legend()

    def histogram_lines_graph(self, data1, data2, title):
        keys = set(data1.keys()).union(set(data2.keys()))
        values = range(len(keys))

        # print(values)
        plt.plot(values, [data1.get(key, 0)
                 for key in keys], 'b-', label='Plaintext')
        plt.plot(values, [data2.get(key, 0)
                 for key in keys], 'r-', label='Ciphertext')

        plt.title(title)
        plt.xlabel("Character")
        plt.ylabel("Frequency")
        plt.xticks(values, keys)
        plt.legend()

    def plot_ascii_frequency(self, string, title):
        ascii_values = [ord(char) for char in string]
        ascii_counts = Counter(ascii_values)

        keys = list(ascii_counts.keys())
        values = list(ascii_counts.values())

        sorted_keys = sorted(keys)
        labels = [str(key) for key in sorted_keys]

        plt.figure(figsize=(40, 10))
        plt.bar(range(len(keys)), values)
        plt.xlabel("Kode ASCII")
        plt.ylabel("Frekuensi")
        plt.title(title)
        plt.xticks(range(len(keys)), labels, rotation='vertical')
        plt.show()

    # def plot_ascii_frequency(self, string, title):
    #     ascii_values = [ord(char) for char in string]
    #     ascii_counts = Counter(ascii_values)

    #     sorted_ascii_values = sorted(ascii_counts.keys())
    #     frequencies = [ascii_counts[val] for val in sorted_ascii_values]
    #     plt.figure(figsize=(30, 10))
    #     plt.bar(sorted_ascii_values, frequencies)
    #     plt.xlabel('Kode ASCII')
    #     plt.ylabel('Frekuensi')
    #     plt.title(title)
    #     plt.xticks(sorted_ascii_values, [
    #                str(val) for val in sorted_ascii_values], rotation='vertical')
    #     # plt.grid(True)
    #     plt.show()
