import json
import PySimpleGUI as sg
from logging_code import logger
from step4 import main

try:
    with open("settings.json") as infile:
        settings_ojbect = json.load(infile)
        # print(settings_ojbect)
    logger.info("settings json file opened")

except:
    logger.error("settings json file not found")

input_folder = settings_ojbect["user_settings"]["user_input_folder"]
logger.info("input folder accessed")

# if input_folder in [None or ""]:
#     settings_ojbect["user_settings"]["user_input_folder"] = settings_ojbect[
#         "default_settings"
#     ]["user_input_folder"]

output_folder = settings_ojbect["user_settings"]["user_output_folder"]
# if output_folder in [None or ""]:
#     settings_ojbect["user_settings"]["user_output_folder"] = settings_ojbect[
#         "default_settings"
#     ]["user_output_folder"]


def update(key_name):
    infolder = values["-IN-"]
    outfolder = values["-OUT-"]

    if infolder != input_folder:
        if infolder == "":
            pass
        else:
            settings_ojbect[key_name]["user_input_folder"] = infolder

    if outfolder != output_folder:
        if outfolder == "":
            pass

        else:
            settings_ojbect[key_name]["user_output_folder"] = outfolder
    with open("settings.json", "w") as outfile:
        json.dump(settings_ojbect, outfile)


layout = [
    [sg.Text("Please Select the Input Folder")],
    [
        sg.Frame(
            layout=[
                [
                    sg.Checkbox(
                        "Restore Defaults",
                        size=(17, 1),
                        key="-RESTORE-",
                        enable_events=False,
                    ),
                    sg.Button(
                        button_text="Confirm Restore", size=(14, 1), key="-CONFIRM-"
                    ),
                ],
                [
                    sg.Text("Choose an Input Folder: ", size=(20, 1)),
                    sg.Input(default_text=input_folder, size=(50, 1)),
                    sg.FolderBrowse(
                        initial_folder=input_folder,
                        change_submits=True,
                        key="-IN-",
                    ),
                ],
                [
                    sg.Text("Choose an Output Folder: ", size=(20, 1)),
                    sg.Input(default_text=output_folder, size=(50, 1)),
                    sg.FolderBrowse(
                        initial_folder=output_folder,
                        change_submits=True,
                        key="-OUT-",
                    ),
                ],
                [
                    sg.Checkbox(
                        "Set Defaults",
                        size=(17, 1),
                        key="-SET-",
                        enable_events=False,
                    ),
                    sg.Button(
                        button_text="Set Default", size=(14, 1), key="-CONFIRM2-"
                    ),
                ],
            ],
            title="choose your files",
            title_color="white",
            relief=sg.RELIEF_SUNKEN,
            tooltip="Use these to set flags",
        )
    ],
    [
        sg.Submit(size=(6, 1)),
        sg.Cancel(size=(6, 1)),
        sg.Button(button_text="Start", size=(6, 1), key="-START-"),
        sg.Button(button_text="Exit", size=(6, 1), key="-EXIT-"),
    ],
]
# begin with a blank form
form = sg.FlexForm(
    "Choose contract notes in Pdf formats for conversion", layout, finalize=True
)
while True:
    event, values = form.read()
    # event, values = form.Read()
    if event == sg.WIN_CLOSED or event == "Cancel" or event == "-EXIT-":
        logger.info("window closed or cancelled or exit")
        break
    elif event == "Submit":
        update("user_settings")
        form.refresh()

    elif event == "-CONFIRM-" and values["-RESTORE-"] == True:
        settings_ojbect["user_settings"]["user_input_folder"] = settings_ojbect[
            "default_settings"
        ]["user_input_folder"]

        settings_ojbect["user_settings"]["user_output_folder"] = settings_ojbect[
            "default_settings"
        ]["user_output_folder"]
        print("restore defaults")
        sg.Popup(
            "'        defaults restored                                '   ",
            keep_on_top=True,
            title="defaults restored",
        )
        with open("settings.json", "w") as outfile:
            json.dump(settings_ojbect, outfile)
        form.refresh()

    elif event == "-CONFIRM2-" and values["-SET-"] == True:
        update("default_settings")
        print("restore defaults")
        sg.Popup(
            "'        new folders defined                                '   ",
            keep_on_top=True,
            title="defaults restored",
        )
        with open("settings.json", "w") as outfile:
            json.dump(settings_ojbect, outfile)

        logger.info("defaults restored")
        form.refresh()

    elif event == "-START-":
        # print("START")
        main()
        sg.Popup(
            "'        files converted                                '   ",
            keep_on_top=True,
            title="'     converting files     '",
        )
    logger.info("files converted")

form.close()
