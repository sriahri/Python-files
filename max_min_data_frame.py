import pandas as pd


def min_max(s):
    df = pd.read_csv("Advertising.csv")
    maximum = df[s].max()
    minimum = df[s].min()
    average = df[s].mean()

    return maximum, minimum, average


if __name__ == '__main__':
    maxi, mini, avg = min_max('TV')
    print('Maximum :', maxi)
    print('Minimum :', mini)
    print('Average :', avg)
