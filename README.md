Net2Shell

Net2Shell is a simple Python tool that converts .NET exe files into shellcode. This tool reads the given .NET exe file, finds the entry point using the PE (Portable Executable) format, and extracts the relevant code section as shellcode. The shellcode is then printed to the console in hexadecimal format.

Usage:

To use the application, you can use the following command in the terminal:

python exe2shell.py application.exe

- exe2shell.py: Python script.
- application.exe: Path to the .NET exe file you want to convert.

For example:

python exe2shell.py example.exe

This command reads the example.exe file, generates the shellcode, and prints it to the console in hexadecimal format.

Requirements:

The application requires the following Python modules to be installed:

- pefile

You can use the requirements.txt file to install the required modules:

pip install -r requirements.txt

License:

This project is licensed under the MIT License. For more information, see the LICENSE file.
