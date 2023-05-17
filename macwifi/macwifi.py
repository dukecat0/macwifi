import subprocess
import sys

PATH_OF_AIRPORT = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"
PATH_OF_NETWORK_SETUP = '/usr/sbin/networksetup'


if "darwin" not in sys.platform:
    raise Exception("macwifi only works on macOS.")


def get_wifi_info():
    """Get the information about the connected WiFi."""
    process = subprocess.Popen([PATH_OF_AIRPORT, "-I"], stdout=subprocess.PIPE)
    out, err = process.communicate()
    process.wait()
    return out.decode("utf-8")


def get_ssid():
    """Get the SSID of the connected WiFi."""
    process = subprocess.Popen([PATH_OF_AIRPORT, "-I"], stdout=subprocess.PIPE)
    out, err = process.communicate()
    process.wait()
    output = {}
    for line in out.decode("utf-8").split("\n"):
        if ": " in line:
            key, value = line.split(": ")
            key = key.strip()
            value = value.strip()
            output[key] = value

    return output["SSID"]


def get_rssi():
    """Get the signal strength of the connected WiFi."""
    process = subprocess.Popen([PATH_OF_AIRPORT, "-I"], stdout=subprocess.PIPE)
    out, err = process.communicate()
    process.wait()
    output = {}
    for line in out.decode("utf-8").split("\n"):
        if ": " in line:
            key, value = line.split(": ")
            key = key.strip()
            value = value.strip()
            output[key] = value

    return output["agrCtlRSSI"]


def is_wifi_available(ssid: str) -> bool:
    """Check if the given SSID is available."""
    return ssid in list()


def connect(ssid : str, password : str, device : str = "en0") -> bool or Exception:
    """Connect to a WiFi network.

    Args:
        ssid: The SSID of the WiFi.
        password: The password of the WiFi.
        device: The device name of the WiFi. Default is "en0".
    """
    if not is_wifi_available(ssid):
        raise Exception("The SSID is incorrect.")

    print(f"Connecting to {ssid}...")
    process = subprocess.Popen(
        [PATH_OF_NETWORK_SETUP, "-setairportnetwork", device, ssid, password],
        stdout=subprocess.PIPE,
    )
    out, err = process.communicate()
    process.wait()
    result = out.decode("utf-8")
    if not result:
        return True
    elif "Could not find network" or "Failed to join network" in result:
        raise Exception("Seems that the SSID or the password is incorrect.")


def turn_on():
    """Turn on the WiFi."""
    process = subprocess.Popen(
        [PATH_OF_NETWORK_SETUP, "-setnetworkserviceenabled", "Wi-Fi", "on"],
        stdout=subprocess.PIPE,
    )
    out, err = process.communicate()
    process.wait()
    _ = out.decode("utf-8")
    if process.returncode == 0:
        return True
    else:
        raise Exception("Failed to turn on the WiFi.")


def turn_off():
    """Turn off the WiFi."""
    process = subprocess.Popen(
        [PATH_OF_NETWORK_SETUP, "-setnetworkserviceenabled", "Wi-Fi", "off"],
        stdout=subprocess.PIPE,
    )
    out, err = process.communicate()
    process.wait()
    _ = out.decode("utf-8")
    if process.returncode == 0:
        return True
    else:
        raise Exception("Failed to turn off the WiFi.")


def list():
    """List all available WiFi networks."""
    process = subprocess.Popen([PATH_OF_AIRPORT, "-s"], stdout=subprocess.PIPE)
    out, err = process.communicate()
    process.wait()
    result = out.decode("utf-8")
    return result
