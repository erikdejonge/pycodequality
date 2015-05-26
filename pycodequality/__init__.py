# coding=utf-8
"""
Give a rating for a python folder

Usage:
  pycodequality.py [options] <folder>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : pycodequality
created : 26-05-15 / 15:00
"""
from arguments import Arguments


def main():
    """
    main
    """
    arguments = Arguments(__doc__)
    print(arguments)


if __name__ == "__main__":
    main()
