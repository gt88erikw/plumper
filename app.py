import pandas as pd


def run(csv_path):
    df = pd.read_csv(csv_path)

    return df.head()



if __name__ == "__main__":
    print(run ("C:/TempStuff/bae146-200/CLB_-10.csv"))