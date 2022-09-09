"""Command-line interface."""
import click
import time
from is_activetime import is_activetime
from is_workday import is_workday


@click.command()
@click.version_option()
def main() -> None:
    """slack_status_updater."""

    # TODO get config

    # loop
    while True:
        while True:
            # check working day
            if not is_workday(
                holidays_ignored=False
            ):  # TODO get holidays_ignored from config
                break
            # check active time
            if not is_activetime(schedule):
                break
            # get MAC
            # update SLACK status for 10 minutes
        # sleep for 4 minutes
        time.sleep(4 * 60)  # TODO get from config


if __name__ == "__main__":
    main(prog_name="slack_status_updater")  # pragma: no cover
