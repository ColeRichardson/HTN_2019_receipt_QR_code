#!/usr/bin/python

import sys, getopt

def main(argv):
    receipt = argv[0]
    output_filename = argv[1]
    link = generate_qr(receipt, output_filename)

def generate_qr(link, output_filename):
    import qrcode
    from qrcode.image.pure import PymagingImage
    img = qrcode.make(link)
    img.save(output_filename)

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("Usage: python qr.py [input] [output_filename]")
    main(sys.argv[1:])
