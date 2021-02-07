#! /usr/bin/env python

"""358 turn signal

Query the turn signal status of a Nissan Leaf using an ELM327 compatible diagnostic
tool.

Tested on the following vehicles:

* AZE0
"""

import serial

elm = serial.Serial("/dev/ttyUSB0", 38400, timeout=5)

elm.write(b"ATZ\r")  # reset all
print(elm.read_until(b"\r\r>").decode())

elm.write(b"ATI\r")  # print version ID
print(elm.read_until(b"\r\r>").decode())

elm.write(b"ATL1\r")  # line feeds on
print(elm.read_until(b"\r\n>").decode())

elm.write(b"ATH1\r")  # headers on
print(elm.read_until(b"\r\n>").decode())

elm.write(b"ATS1\r")  # print spaces on
print(elm.read_until(b"\r\n>").decode())

elm.write(b"ATAL\r")  # allow long messages
print(elm.read_until(b"\r\n>").decode())

elm.write(b"ATSP6\r")  # set protocol ISO 15765-4 CAN (11 bit 500 kBd)
print(elm.read_until(b"\r\n>").decode())

elm.write(b"ATCRA 358\r")  # set CAN receive address
print(elm.read_until(b"\r\n>").decode())

elm.write(b"ATMA\r")  # monitor all messages

try:
    while True:
        print(elm.read_until(b"\r\n").decode(), flush=True)
except KeyboardInterrupt:
    print("Keyboard interrupt")

elm.close()
