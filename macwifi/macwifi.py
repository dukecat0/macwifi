import subprocess
import sys

PATH_OF_AIRPORT = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"

if not "darwin" in sys.platform:
    raise Exception("macwifi only works on macOS.")


def get_wifi_info():
    """Get the information about the connected WiFi."""
    process = subprocess.Popen([PATH_OF_AIRPORT, "-I"], stdout=subprocess.PIPE)
    out, err = process.communicate()
    process.wait()
    print(out.decode("utf-8"))


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

    print("SSID: " + output["SSID"])


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

    print("RSSI: " + output["agrCtlRSSI"])


def connect(ssid, password):
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
        print("Successfully connected to " + ssid + ".")
    elif "Could not find network" or "Failed to join network" in result:
        print("Seems that the SSID or the password is incorrect. Please try again.")


def turn_on():
    """Turn on the WiFi."""
    print("Turning on the WiFi...")
    process = subprocess.Popen(
        ["networksetup", "-setnetworkserviceenabled", "Wi-Fi", "on"],
        stdout=subprocess.PIPE,
    )
    out, err = process.communicate()
    process.wait()
    result = out.decode("utf-8")
    if process.returncode == 0:
        print("Successfully turned on the WiFi.")
    else:
        print("Failed to turn on the WiFi.")


def turn_off():
    """Turn off the WiFi."""
    print("Turning off the WiFi...")
    process = subprocess.Popen(
        ["networksetup", "-setnetworkserviceenabled", "Wi-Fi", "off"],
        stdout=subprocess.PIPE,
    )
    out, err = process.communicate()
    process.wait()
    result = out.decode("utf-8")
    if process.returncode == 0:
        print("Successfully turned off the WiFi.")
    else:
        print("Failed to turn off the WiFi.")


def list():
    """List all available WiFi networks."""
    print("Listing all available WiFi networks...")
    process = subprocess.Popen([PATH_OF_AIRPORT, "-s"], stdout=subprocess.PIPE)
    out, err = process.communicate()
    process.wait()
    result = out.decode("utf-8")
    print(result)
