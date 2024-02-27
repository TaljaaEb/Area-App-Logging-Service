import subprocess

#message = output.stdout.read()
def main():
    command = "tcpdump.exe -nvvvXi \Device\{048A3128-F966-452C-B32D-5DDF79A39821}"
    output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)

    while True:
        line = output.stdout.readline()
        print(line)

if "__name__" == "__main__":
    main()
