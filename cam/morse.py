import json
import time
from machine import Pin

led = Pin(4, Pin.OUT)

TABLE = "morse_table.json"

f = open(TABLE, "r")
translate = json.loads(f.read())
f.close()

print("Morse table parsed!")

LONG  = 1
SHORT = 0

SHORT_DURATION = 0.5
LONG_DURATION  = 1.5
SPACE_DURATION = 2

BETWEEN_CHAR_DURATION = 0.3

def beep(duration: float) -> None:
    led.value(1)
    time.sleep(duration)
    led.value(0)
    time.sleep(BETWEEN_CHAR_DURATION)

def space() -> None:
    beep(SPACE_DURATION)

def long() -> None:
    beep(LONG_DURATION)

def short() -> None:
    beep(SHORT_DURATION)

SIGNAL = {
        LONG : long,
        SHORT: short
        }

def encode(sentence: str) -> None:

    for char in sentence:

        if char == " ":
            space()
            continue

        signals = translate[ char ]
        for signal in signals:
            SIGNAL[ signal ]()
