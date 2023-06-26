import matplotlib.pyplot as plt


class PlotHistogramLine:
    def plot_histogram(data1, data2, title):
        keys = set(data1.keys()).union(set(data2.keys()))
        values = range(len(keys))
        plt.plot(values, [data1.get(key, 0)
                 for key in keys], 'b-', label='Plaintext')
        plt.plot(values, [data2.get(key, 0)
                 for key in keys], 'r-', label='Ciphertext')

        plt.title(title)
        plt.xlabel("Character")
        plt.ylabel("Frequency")
        plt.xticks(values, keys)
        plt.legend()
