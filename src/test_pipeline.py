# test transform data

def test_transform_data():
    prices = [10, 20, 30]
    result = transform_data(prices)
    assert result == [10, 20, 30]
