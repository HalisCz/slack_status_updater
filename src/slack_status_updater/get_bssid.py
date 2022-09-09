from sys import platform

from get_bssid_darwin import get_bssid_darwin


def get_bssid(os=platform.lower(), interface=""):
    """
    Gets BSSID of AP that WiFi interface is connected to

    :param os: string of a current OS platform
    :param interface: name of WiFi interface
    :return: string bssid of WiFi AP that interface is connected to
    """

    if os == "darwin":
        return get_bssid_darwin()
    elif os == "linux":
        raise Exception("Sorry, platform Linux is not supported yet :-(")
        return get_bssid_linux(interface)
    elif os == "windows":
        raise Exception("Sorry, platform Windows is not supported yet :-(")
        return get_bssid_windows(interface)
    else:
        raise Exception(f"Sorry, platform '{str(os)}' is not supported")
        return False  # I love to watch the world burn :)
