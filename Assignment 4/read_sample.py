print("Reading file content:")
try:
    with open("sample.txt", "r") as fh:
        print(f"Line1: {fh.readline()}")
        print(f"Line2: {fh.readline()}")
except FileNotFoundError:
    print("File not found")