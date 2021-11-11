# macwifi

Macwifi is a Python module that helps you to manage the WiFi on macOS.

## Installation

```
pip install macwifi
```
## Example

Connect to a WiFi network:

```python
import macwifi

macwifi.connect("MyWiFi", "password")
```

Done!

## Usage

List all available WiFi networks.

`list()`

Get the information about the connected WiFi.

`get_wifi_info()`

Get the SSID of the connected WiFi.

`get_ssid()`

Get the signal strength of the connected WiFi.

`get_rssi()`

Connect to a WiFi network.

`connect(ssid, password)`

Turn on the WiFi.

`turn_on()`

Turn off the WiFi.

`turn_off()`
