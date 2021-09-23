import re
import json
from pathlib import Path, PurePath


def header(input):
    header_list = []
    start_string = ""
    with open(input) as reader:
        for line in reader:
            start_string == re.match(r"w{3}-w{3}-w{3}")
            header_list += start_string
            return header_list
