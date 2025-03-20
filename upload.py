"""Upload radio image."""
import argparse
import lab5RM as lab

if __name__ == '__main__':
    try:
        ap = argparse.ArgumentParser()
        ap.add_argument("--image",
                            required=True,
                            help="Name of radio image file.")
        ap.add_argument("-s", "--serial",
                            required=False,
                            default = lab.Port,
                            help="Name of radio image file.")
        args = ap.parse_args()
        with lab.create_serial(args.serial) as s:
            lab.upload(args.image, s)
    except KeyboardInterrupt:
        None

