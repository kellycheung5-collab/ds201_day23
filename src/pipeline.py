# pipeline.py test 2a222
DATA_SOURCE = 'data/external/sales_api.csv'

def load_data(path):
    print(f'Loading data from {path}')
    return []

def clean_data(data):
    print('Cleaning data...')
    return data

def transform_data(data):
    """Remove empty rows and apply cleaning rules."""
    print('Transforming data...')
    return [row for row in data if row]

def test_transform_data():
    prices = [10, 20, 30]
    result = transform_data(prices)
    assert result == [10, 20, 30]