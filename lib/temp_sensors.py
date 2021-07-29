#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

# 4.7k resistor between 3.3v and data signal
# This is my own lib for the DS18B20 waterproof sensor
# Based on the example from https://docs.pycom.io/tutorials/hardware/owd/

import time
from machine import Pin

from onewire import DS18X20
from onewire import OneWire

from dth import DTH

def get_temp_DS18S20(pin):
    ow = OneWire(Pin("P" + str(pin)))
    temp = DS18X20(ow)

    temp.start_conversion()
    time.sleep(1)

    if temp.read_temp_async() is not None:
        return temp.read_temp_async()

def get_temp_DHT22(pin):
    dht22 = DTH(Pin("P" + str(pin), mode=Pin.OPEN_DRAIN),1)

    result = dht22.read()
    if result.is_valid():
        return result.temperature

def get_humidity_DHT22(pin):
    dht22 = DTH(Pin("P" + str(pin), mode=Pin.OPEN_DRAIN),1)

    result = dht22.read()
    if result.is_valid():
        return result.humidity

print(get_temp_DS18S20)
