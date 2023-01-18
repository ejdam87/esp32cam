import wifi
import webserver

## SSID & PASSWORD of your network
## ---
NET_PATH = "credentials.secret"

with open( NET_PATH, "r" ) as f:
    SSID, PASSWD = f.read( ).split( "\n" )
## ---

wlan = wifi.connect( SSID, PASSWD )
print( "Connected" )

webserver.run( )
