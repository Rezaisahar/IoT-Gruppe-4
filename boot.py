import time
import network

# 1. Configuration
WIFI_SSID = "Rechnernetze"
WIFI_PASS = "rnFIW625"


# 2. Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASS)
print("Connecting...")
while not wlan.isconnected():
    time.sleep(1)
print("Wifi ok")



