#!/usr/bin/env python3

import argparse

from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Display.SimpleGui import init_display
from PIL import Image

parser = argparse.ArgumentParser(prog="Step to Image convertor", description="Converts a step file to an image")
parser.add_argument("-i", "--input", help="Input step file")
parser.add_argument("-o", "--output", help="Output image file")
parser.add_argument("-w", "--width", help="Width of the output image in points")

args = parser.parse_args()


def generate_img(input: str, output: str, width: int, height: int) -> None:
    img = Image.new("RGB", (width, height), color=(255, 255, 255, 0))
    step_reader = STEPControl_Reader()
    step_reader.ReadFile(input)
    step_reader.TransferRoot()
    shape = step_reader.Shape()
    display = init_display()

    img.save(output)


if __name__ == "__main__":
    input_file: str = args.input
    output_file: str = args.output
    width: int = int(args.width)
    height = width
    generate_img(input_file, output_file, width, height)
