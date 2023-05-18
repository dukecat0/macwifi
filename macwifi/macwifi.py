import subprocess
import sys
from typing import Optional

PATH_OF_AIRPORT: str = (
    "/System/Library/PrivateFrameworks/"
    "Apple80211.framework/Versions/Current/Resources/airport"
)

if "darwin" not in sys.platform:
    raise Exception("macwifi only works on macOS.")


def get_wifi_info() -> str:
    """Get the information about the connected WiFi."""
    process = subprocess.Popen([PATH_OF_AIRPORT, "-I"], stdout=subprocess.PIPE)
    out, err = process.communicate()
    process.wait()
    return out.decode("utf-8")


def get_ssid() -> str:
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


def get_rssi() -> str:
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


def connect(ssid: str, password: str) -> Optional[bool]:
    """Connect to a WiFi network.

    Args:
        ssid: The SSID of the WiFi.
        password: The password of the WiFi.
    """
    print(f"Connecting to {ssid}...")
    process = subprocess.Popen(
        ["networksetup", "-setairportnetwork", "en0", ssid, password],
        stdout=subprocess.PIPE,
    )
    out, err = process.communicate()
    process.wait()
    result = out.decode("utf-8")
    if not result:
        return True
    elif "Could not find network" or "Failed to join network" in result:
        raise Exception("SSID or password may be incorrect.")


def turn_on() -> Optional[bool]:
    """Turn on the WiFi."""
    process = subprocess.Popen(
        ["networksetup", "-setnetworkserviceenabled", "Wi-Fi", "on"],
        stdout=subprocess.PIPE,
    )
    out, err = process.communicate()
    process.wait()
    _ = out.decode("utf-8")
    if process.returncode == 0:
        return True
    else:
        raise Exception("Failed to turn on the WiFi.")


def turn_off() -> Optional[bool]:
    """Turn off the WiFi."""
    process = subprocess.Popen(
        ["networksetup", "-setnetworkserviceenabled", "Wi-Fi", "off"],
        stdout=subprocess.PIPE,
    )
    out, err = process.communicate()
    process.wait()
    _ = out.decode("utf-8")
    if process.returncode == 0:
        return True
    else:
        raise Exception("Failed to turn off the WiFi.")


def list() -> str:
    """List all available WiFi networks."""
    process = subprocess.Popen([PATH_OF_AIRPORT, "-s"], stdout=subprocess.PIPE)
    out, err = process.communicate()
    process.wait()
    result = out.decode("utf-8")
    return result
