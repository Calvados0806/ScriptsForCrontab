#!/usr/bin/env python3

from matplotlib import pyplot as plt

def read_file(path):
    ls = []
    with open(path, 'r') as file:
        for line in file:
            ls.append(float(line.strip()))

    return ls

def main():
    usd = read_file("USD.csv")
    eur = read_file("EUR.csv")

    x_range = range(len(usd))
    plt.subplot(211)
    plt.plot(x_range, usd, 'r', label="USD")
    plt.grid(True)
    plt.title("Exchange rate\nUSD, EUR")
    plt.ylabel("UAN")
    plt.legend()
    plt.subplot(212)
    plt.plot(x_range, eur, 'b', label="EUR")
    plt.xlabel("Time")
    plt.ylabel("UAN")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
