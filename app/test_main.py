import pytest
from unittest import mock
from datetime import datetime

from app.main import outdated_products


@pytest.mark.parametrize(
    "data,today,result",
    [
        (
            [{
                "name": "salmon",
                "expiration_date": datetime(2022, 2, 10).date(),
                "price": 600
            }],
            datetime(2022, 2, 11).date(),
            ["salmon"]
        ),
        (
            [{
                "name": "chicken",
                "expiration_date": datetime(2022, 2, 5).date(),
                "price": 120
            }],
            datetime(2022, 2, 4).date(),
            []
        )
    ]
)
def test_outdated_products(
        data: list[dict],
        today: datetime,
        result: list[str]
) -> None:
    with mock.patch("datetime.date") as mock_time:
        mock_time.today = lambda: today
        assert outdated_products(data) == result
