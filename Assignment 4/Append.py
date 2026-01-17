text = input("Enter text to write in file: ")
fh = open("append.txt", "wt")
fh.write(f"{text}")
fh.close()
print(f"Text written in append.txt : {text}")

append = input("Enter text to append to file: ")
fh = open("append.txt", "at")
fh.write(f"\n{append}")
fh.close()
print(f"Text appended in append.txt : {append}")

fh = open("append.txt", "rt")
print(fh.read())
fh.close()

