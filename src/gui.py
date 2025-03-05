#Nicholas Hoven 2025
import tkinter as tk
from tkinter import font
from tkinter import ttk
from pathlib import Path
from state_data import *

root = tk.Tk()
current_state = State("", "", "", "")

def clear_menu(): #this will completely clear the GUI menu
    for widget in root.winfo_children():
        widget.destroy()

def clear_labels():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()


def display_state_data(state_name):
    clear_menu()
    display_main_menu()
    custom_font = font.Font(family=font.nametofont("TkDefaultFont").actual("family"), size=18)
    if state_name != "":
        for state in states:
            if state.get_name() == state_name:
                current_state = state
                print(current_state.get_name())
                data = (
                    f"{state.name}\n"
                    f"Abbreviation: {state.abbreviation}\n"
                    f"Zip Code: {state.zip_code}\n"
                    f"FIPS Code: {state.fips_code}"
                )
                label = tk.Label(root, text=data, font = custom_font)
                label.place(x=170, y=33)


def display_main_menu():
    clear_menu()
    root.title("Quick States")
    root.geometry("375x200")
    state_names = [state.get_name() for state in states]
    combobox = ttk.Combobox(root, values = state_names)
    combobox.place(x = 5)
    combobox.bind("<<ComboboxSelected>>", lambda event: display_state_data(combobox.get()))
    copy_zip_button = tk.Button(root, text = "Copy Zip")
    copy_zip_button.place(x = 152)
    copy_fip_button = tk.Button(root, text = "Copy Fip")
    copy_fip_button.place(x = 214)
    copy_bruno_button = tk.Button(root, text = "Copy to Bruno")
    copy_bruno_button.place(x = 275)


def run_gui():
    display_main_menu()
    root.mainloop()