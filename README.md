# QuickStates

QuickStates is a companion application designed to streamline the process of viewing and importing state testing data within Bruno. It simplifies the retrieval of state-specific information, such as ZIP codes and FIPS codes, and facilitates the creation of Bruno testing scripts.

## Description

QuickStates provides a user-friendly GUI with three key functionalities:

* **Copy Zip:** Copies the ZIP code of the selected state to the clipboard.
* **Copy Fip:** Copies the FIPS code of the selected state to the clipboard.
* **Copy to Bruno:** Generates a Bruno testing script containing all the current state data and copies it to the clipboard, ready to be pasted into Bruno.

This application is intended to enhance the workflow of developers and testers using Bruno by providing quick access to essential state data.

## Installation

1.  Download the `QuickStates.exe` executable file.
2.  Run the `QuickStates.exe` file.

No further installation steps are required.

## Usage

1.  Launch the QuickStates application by running the `QuickStates.exe` file.
2.  Select the desired state from the provided list.
3.  Use the following buttons to perform the desired action:
    * **Copy Zip:** Click this button to copy the selected state's ZIP code to your clipboard.
    * **Copy Fip:** Click this button to copy the selected state's FIPS code to your clipboard.
    * **Copy to Bruno:** Click this button to generate a Bruno testing script based on the selected state's data and copy it to your clipboard.
4.  Paste the copied data or Bruno script into the appropriate application (e.g., Bruno, text editor).

## Examples

* **Copying a ZIP code:**
    1.  Select "California" from the state list.
    2.  Click "Copy Zip."
    3.  Paste the ZIP code (e.g., 90001) into your desired location.

* **Generating a Bruno testing script:**
    1.  Select "Texas" from the state list.
    2.  Click "Copy to Bruno."
    3.  Open Bruno and paste the generated script into a new request. This will set up your test request with the data from Texas.

## Contributing

Contributions are not currently being accepted.

## License

This project is currently unlicensed.

## Acknowledgments

* This application is designed to work in conjunction with the Bruno API testing tool.
