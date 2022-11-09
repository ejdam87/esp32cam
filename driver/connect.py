import network

ssid_ = "Vodafone-6B45"
wp2_pass = "2jE7vbXxHpkxsjFy"

def connect() -> None:
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid_, wp2_pass)
