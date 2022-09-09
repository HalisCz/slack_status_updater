import pytest
from datetime import datetime
import json
from slack_status_updater import is_activetime

SCHEDULE_SAMPLE = json.loads(
    """
{
  "schedule": {
    "default": [
      "08:00-09:00"
    ],
    "monday": [
      "09:00-10:00",
      "11:20-14:00"
    ],
    "tuesday": null,
    "wednesday": null,
    "thursday": null,
    "saturday": null,
    "sunday": null
  }
}
"""
)


# TODO addd malformed schedule test
@pytest.mark.parametrize(
    "schedule, timestamp, result",
    [
        (
            SCHEDULE_SAMPLE,
            datetime(year=2022, month=10, day=24, hour=12, minute=0),
            True,
        ),
        (
            SCHEDULE_SAMPLE,
            datetime(year=2022, month=10, day=24, hour=23, minute=12),
            False,
        ),
        (
            SCHEDULE_SAMPLE,
            datetime(year=2022, month=10, day=28, hour=8, minute=0),
            True,
        ),
    ],
)
def test_is_activetime(schedule, timestamp, result):
    # check for expected result
    assert is_activetime.is_activetime(schedule=schedule, timestamp=timestamp) == result
