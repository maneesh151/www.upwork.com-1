from step2_pdf_txt import output_folder
from step3_txt_json import header
from pathlib import Path, PurePath
import json
from logging_code import logger


def main():

    path = Path(output_folder).rglob("*.txt")

    # json_output = input_file.replace(".csv", ".json")
    for text_file in [file for file in path]:

        with open(json_file, "w") as outfile:
            json.dump(trade_dict, outfile, indent=4, sort_keys=False)
            # logger.error(Exception(f"Please check main"))
            # logger.warning(Exception(f"Please check main"))
    return 0


if __name__ == "__main__":
    main()
