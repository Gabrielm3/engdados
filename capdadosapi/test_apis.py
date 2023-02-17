import datetime

from apis import DaySummaryApi


def test_get_endpoint_BTC():
    date = datetime.date(2023, 2, 10)
    api = DaySummaryApi(coin="BTC")
    actual = api._get_endpoint(date=date)
    expected = "https://www.mercadobitcoin.net/api/BTC/day-summary/2023/2/10"
    assert actual == expected


def test_get_endopoint_ETH():
    date = datetime.date(2023, 2, 10)
    api = DaySummaryApi(coin="EH")
    actual = api._get_endpoint(date=date)
    expected = "https://www.mercadobitcoin.net/api/ETH/day-summary/2023/2/10"
    assert actual == expected
