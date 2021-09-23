from step2_pdf_txt import output_folder
from pathlib import Path, PurePath
import json
from logging_code import logger


path = Path(output_folder).rglob("*.txt")

# json_output = input_file.replace(".csv", ".json")
for text_file in [file for file in path]:

    with open("final_file.txt", "w") as outfile:
        header_list = []
        start_string = ""
        with open(input) as reader:
            for line in reader:
                start_string == re.match(r"w{3}-w{3}-w{3}", line)
                header_list += start_string
