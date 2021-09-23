import json
import subprocess
from pathlib import Path, PurePath
import re
from logging_code import logger
import PySimpleGUI as sg


with open("settings.json") as infile:
    settings = json.load(infile)
    logger.info("settings file opened in step 2 ")

input_folder = settings["user_settings"]["user_input_folder"]
output_folder = settings["user_settings"]["user_output_folder"]
input_path_folder = Path(input_folder)
output_path_folder = Path(output_folder)

if not output_path_folder.is_dir():
    # directory does not exists
    logger.error("directory output does not exist")
    sg.Popup(
        "'        directory output does not exist , creating it......                           '   ",
        keep_on_top=True,
        title="--------ERROR---------",
    )
    output_path_folder.mkdir(parents=True, exist_ok=True)

# /------------------

if not input_path_folder.is_dir():
    # directory does not exists
    logger.error("directory input_path does not exist")
    sg.Popup(
        "'        directory input does not exist , create and copy pdf files in it                     '   ",
        keep_on_top=True,
        title="--------ERROR---------",
    )
input_path_files = input_path_folder.rglob("*.pdf")


program = "pdftotext.exe"

for pdf_file in [file for file in input_path_files]:
    text_file = PurePath(output_folder, pdf_file.name.replace(".pdf", ".txt"))

    process = subprocess.run(
        [
            program,
            "-table",
            pdf_file,
            text_file,
        ],
        text=True,
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.DEVNULL,
    )
    logger.info("pdf converted to txt")

    if process.returncode == 0:
        with open(text_file) as reader, open(text_file.name + ".tmp", "w") as writer:
            lines = reader.read()
            mod_lines = re.sub("^\s*$\r?\n", "", lines)
            mod_lines = re.sub("\n\n", "\n", lines)
            writer.write(mod_lines)
        # p = Path(text_file)
        temp_file = Path(text_file.name + ".tmp")
        temp_file.replace(text_file)
        logger.info("text files cleaned , no blanks")

    else:
        logger.error("text files not converted")
