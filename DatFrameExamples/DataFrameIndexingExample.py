import numpy as np
import pandas as pd


def main():
    array = np.random.randn(4, 2)
    df = pd.DataFrame(array)
    print(df)

    columns = ['A', 'B']
    df = pd.DataFrame(array, columns=columns)
    print(df)

    indices = ['a', 'b', 'c', 'd']
    df = pd.DataFrame(array, columns=columns, index=indices)
    print(df)

    print(df.loc['a'])


if __name__ == '__main__':
    main()
