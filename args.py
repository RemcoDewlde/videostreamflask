import argparse


def parse_args(args):
    parser = argparse.ArgumentParser(description='Use a specific youtube video to stream ')
    parser.add_argument("--vid", default="25EgbhdVESE", type=str, help="use this command to specify a youtube id")
    args = parser.parse_args()
    return args
