import network

def connect( ssid: str, passwd: str ) -> network.WLAN:
    network.WLAN(network.AP_IF).active( False )  # disable access point
    wlan = network.WLAN( network.STA_IF )
    wlan.active( True )

    wlan.connect( ssid, passwd )
    return wlan
