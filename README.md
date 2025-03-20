## Python scripts that use [CHIRP](https://github.com/kk7ds/chirp) to program a Baofeng AR-5RM radio from the command line.

I use CHIRP on my OpenBSD Lenovo laptop to program my Baofeng AR-5RM. Often I just want to do a quick update to memory and I prefer using the command line for this instead of the UI. These 3 scripts, `download.py`, `upload.py`, and `replace.py` covers everything I need.

Many things to the [CHIRP project](https://www.chirpmyradio.com/projects/chirp/wiki/Home).

### download.py
Download radio image file.

    usage: download.py [-h] [-f IMAGE] [-s SERIAL]
    
    options:
      -h, --help            show this help message and exit
      -f IMAGE, --image IMAGE
                            Name of radio image file.
      -s SERIAL, --serial SERIAL
                            Path to serial device.

### upload.py
Upload radio image file.

    usage: upload.py [-h] --image IMAGE [-s SERIAL]
    upload.py: error: the following arguments are required: --image

### replace.py
Replace radio memory image with a CSV freqency list.

usage: upload.py [-h] --image IMAGE [-s SERIAL]

    options:
      -h, --help            show this help message and exit
      --image IMAGE         Name of radio image file.
      -s SERIAL, --serial SERIAL
                             Name of radio image file.

### Example
From the CHIRP UI, Radio/Query Source/RepeaterBook, download repeaters in your area and save to a CSV file. Then run:

    python replace.py --csv localrepeaters.csv --serial /dev/cuaU0

This downloads the radio image (unless existing image file specified) and replaces the memory with the CSV file.

