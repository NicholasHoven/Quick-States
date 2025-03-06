#Nicholas Hoven 2025
import tkinter as tk
from tkinter import font
from tkinter import ttk
import pyperclip
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

def copy_to_clipboard(text):
    print("CURRENT STATE", current_state.get_name())
    pyperclip.copy(text)

def create_bruno_script():
    global current_state
    if current_state.get_name() != "":
        state_string = 'bru.setVar("state", "' + current_state.get_a_name() + '")'
        zip_string = 'bru.setVar("zip", "' + current_state.get_zip() + '")'
        fip_string = 'bru.setVar("fip", "' + current_state.get_fip() + '")'
        bruno_script = f"{state_string}\n{zip_string}\n{fip_string}"
        copy_to_clipboard(bruno_script)

def display_state_data(state_name):
    clear_menu()
    display_main_menu()
    global current_state
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
                    f"Fips Code: {state.fips_code}"
                )
                label = tk.Label(root, text=data, font = custom_font)
                label.place(x=165, y=33)


def display_main_menu():
    clear_menu()
    root.title("Quick States")
    root.geometry("370x200")
    state_names = [state.get_name() for state in states]
    combobox = ttk.Combobox(root, values = state_names)
    combobox.place(x = 5)
    combobox.bind("<<ComboboxSelected>>", lambda event: display_state_data(combobox.get()))
    copy_zip_button = tk.Button(root, text = "Copy Zip", command = lambda:copy_to_clipboard(current_state.get_zip()))
    copy_zip_button.place(x = 152)
    copy_fip_button = tk.Button(root, text = "Copy Fip", command = lambda:copy_to_clipboard(current_state.get_fip()))
    copy_fip_button.place(x = 214)
    copy_bruno_button = tk.Button(root, text = "Copy to Bruno", command = lambda:create_bruno_script())
    copy_bruno_button.place(x = 275)


def run_gui():
    display_main_menu()
    root.mainloop()