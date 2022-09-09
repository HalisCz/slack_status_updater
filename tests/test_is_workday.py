from datetime import datetime

import pytest

from slack_status_updater import is_workday


@pytest.mark.parametrize(
    "timestamp, holidays_ignored, result",
    [
        (
            datetime(year=2022, month=10, day=28),
            False,
            False,
        ),
        (
            datetime(year=2022, month=10, day=28),
            True,
            True,
        ),
        (
            datetime(year=2022, month=10, day=27),
            False,
            True,
        ),
        (
            datetime(year=2022, month=10, day=29),
            True,
            False,
        ),
    ],
)
def test_is_workday(timestamp, holidays_ignored, result):
    # check for expected result
    assert (
        is_workday.is_workday(timestamp=timestamp, holidays_ignored=holidays_ignored)
        == result
    )
