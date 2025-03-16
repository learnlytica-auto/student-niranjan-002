import pytest
from main import create_dataframe

def test_dataframe_shape():
    df = create_dataframe()
    assert df.shape == (3, 2)  # 3 rows, 2 columns

def test_dataframe_columns():
    df = create_dataframe()
    assert list(df.columns) == ["Name", "Age"]  # Check column names

def test_dataframe_values():
    df = create_dataframe()
    assert df.iloc[1]['Name'] == 'Bob'  # Check if 2nd row, 'Name' is 'Bob'
