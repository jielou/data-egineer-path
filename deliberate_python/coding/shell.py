import subprocess
import sys

print(subprocess)
result = subprocess.run(["/Library/Developer/CommandLineTools/usr/bin/python3","calculator.py","plus","-f 1","-s 2"], stdout=subprocess.PIPE)
print(result.stdout.decode("utf-8"))
print(result.returncode)
if result.returncode:
    sys.exit(result.returncode)
