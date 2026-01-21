import pandas as pd

def create_simple_df():
    data = {'Points': [10, 20], 'Labels': ['A', 'B']}
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = create_simple_df()
    print(df)