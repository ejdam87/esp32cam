
import camera
import picoweb
import machine
import time
import uasyncio as asyncio

led = machine.Pin(4, machine.Pin.OUT)
app = picoweb.WebApp('app')

@app.route('/')
def index(req, resp):

    ## yield from resp.awrite( "Hi" )
    led.on()

    camera.init( 0 )

    # wait for sensor to start and focus before capturing image
    await asyncio.sleep(2)
    buf = camera.capture()

    led.off()
    camera.deinit()

    if len(buf) > 0:
        yield from picoweb.start_response(resp, "image/jpeg")
        yield from resp.awrite(buf)
    else:
        picoweb.http_error(resp, 503)


def run():
    app.run( host="192.168.1.24", port=80, debug=True )
