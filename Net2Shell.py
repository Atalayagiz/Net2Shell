import argparse

def read_exe_file(file_path):
    with open(file_path, 'rb') as f:
        exe_data = f.read()
    return exe_data

def print_shellcode(shellcode):
    shellcode_str = ', '.join(f'0x{byte:02x}' for byte in shellcode)
    print(shellcode_str)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert .NET exe to shellcode.')
    parser.add_argument('exe_file_path', type=str, help='Path to the .NET exe file.')
    args = parser.parse_args()

    exe_file_path = args.exe_file_path

    exe_data = read_exe_file(exe_file_path)
    print_shellcode(exe_data)
