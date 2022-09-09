import subprocess

from loguru import logger


def get_bssid_darwin():
    """
    Gets BSSID of AP that WiFi interface is currently connected to on Darwin platform

    :return: string bssid of WiFi AP that interface is connected to
    """

    wifi_details = subprocess.check_output(
        "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport",
        "-I",
        text=True,
    )

    for line in wifi_details:
        if line.strip().startswith("BSSID"):
            logger.debug(f"BSSID candidate is {line.strip()}")
            return line.strip().split(":", 1)[1].strip()
