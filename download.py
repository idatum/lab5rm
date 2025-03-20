"""Download radio image file."""
import argparse
import lab5RM as lab

if __name__ == '__main__':
    try:
        ap = argparse.ArgumentParser()
        ap.add_argument("-f", "--image",
                            default=lab.Default_filename,
                            help="Name of radio image file.")
        ap.add_argument("-s", "--serial",
                            required=False,
                            default = lab.Port,
                            help="Path to serial device.")
        args = ap.parse_args()
        with lab.create_serial(args.serial) as s:
            print(f'Saving radio to {args.image}')
            lab.download(args.image, s)
    except KeyboardInterrupt:
        None

