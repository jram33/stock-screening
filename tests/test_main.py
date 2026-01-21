from stock_screening.main import create_simple_df 

def test_dataframe_shape():
    df = create_simple_df()
    assert df.shape == (2, 2)