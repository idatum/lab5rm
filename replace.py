"""Replace radio memory with CSV frequency list file."""
import argparse
import time
from serial import Serial
from chirp.errors import RadioError
import lab5RM as lab

Radio_reset_s = 5


def main(csv_filename: str, image_filename: str, s: Serial):
    if image_filename is None:
        radio = lab.sync_radio(s)
        print("Waiting for radio to reset.")
        time.sleep(Radio_reset_s)
    else:
        radio = lab.load_radio(image_filename, s)
    csv_radio = lab.load_generic(csv_filename)
    memory_bounds = radio.get_features().memory_bounds
    for i in range(memory_bounds[0], memory_bounds[1]):
        gen_mem = csv_radio.get_memory(i)
        mem = radio.get_memory(i)
        gen_mem.power = mem.power
        radio.set_memory(gen_mem)
    for _ in range(2):
        try:
            print("Uploading image.")
            radio.sync_out()
        except RadioError as e:
            print(f"Retrying on {e}")
            time.sleep(Radio_reset_s / 2)
            continue
        break

if __name__ == '__main__':
    try:
        ap = argparse.ArgumentParser()
        ap.add_argument("--csv",
                        required=True,
                        help="Name of CSV frequency file.")
        ap.add_argument("--image",
                        required=False,
                        help="Name of radio image file.")
        ap.add_argument("-s", "--serial",
                        required=False,
                        default = lab.Port,
                        help="Path to serial device.")
        args = ap.parse_args()
        with lab.create_serial(args.serial) as s:
            main(args.csv, args.image, s)
    except KeyboardInterrupt:
        None

