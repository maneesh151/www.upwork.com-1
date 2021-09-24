from step2_pdf_txt import output_folder
from pathlib import Path, PurePath
import re
from logging_code import logger

path = Path(output_folder).rglob("*.txt")
_amt = re.compile(r"\d*,?\d*\.\d{2}")

header = {
    "parcel_no": re.compile(r"\w{3}-\w{3}-\w{3}"),
    "owner_name": re.compile(r"\D*"),
    "cy_tax": _amt,
    "cy_penalty": _amt,
    "cy_pubcosts": _amt,
    "py_tax": _amt,
    "py_penalty_interest": _amt,
    "tot_dlnqt_amt": _amt,
}

# json_output = input_file.replace(".csv", ".json")
for text_file in [file for file in path]:

    with open("final_file.txt", "w") as outfile:
        with open(text_file) as reader:
            for line in reader:
                if re.search(header["parcel_no"], line):
                    for head, pattern in header.items():
                        # print(line)
                        for m in pattern.finditer(line):
                            # print(line)
                            print(m.start(), m.end(), m.group())
                            line = line[m.end() :].strip()
                            break
                        # line = line[pattern.finditer(line)[0].end()]
                        # print(head, pattern.finditer(line))
                        # line

                    # parcel_no = re.compile(r"\w{3}-\w{3}-\w{3}")
                    # for m in parcel_no.finditer(line):
                    #     # print(line)
                    #     print(m.start(), m.end(), m.group())
                    #     i=m.end()
                    #     line=line[i:]
