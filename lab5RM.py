"""Baefeng AR-5RM specific library."""
import logging
import argparse
import serial
from chirp import chirp_common
import chirp.drivers.generic_csv as generic
import chirp.drivers.baofeng_uv17Pro as bfradio
import chirp.drivers.baofeng_common as bfc

Port = '/dev/cuaU0'
Timeout = 0.5
Default_filename = 'baofeng.img'


"""Open serial port"""
def create_serial( port: str=Port, timeout: float=Timeout):
    return serial.Serial(port=port,
                         baudrate=115200,
                         timeout=timeout)


"""Create generic radio object from a CSV frequency list."""
def load_generic(csv_filename: str) -> chirp_common.Radio:
    radio = generic.CSVRadio(csv_filename)
    return radio


"""Load a radio image file."""
def load_radio(image_filename: str, s: serial.Serial) -> chirp_common.Radio:
    radio = bfradio.BF5RM(s)
    radio.load(image_filename)
    return radio


"""Download radio image."""
def sync_radio(s: serial.Serial) -> chirp_common.Radio:
    radio = bfradio.BF5RM(s)
    radio.sync_in()
    return radio


"""Upload radio image file."""
def upload(image_filename: str, s: serial.Serial):
    radio = load_radio(image_filename, s)
    radio.sync_out()


"""Download radio image file."""
def download(image_filename: str, s: serial.Serial):
    radio = sync_radio(s)
    radio.save(image_filename)

if __name__ == '__main__':
    print('Library specifically for a Baefeng AR-5RM.')

