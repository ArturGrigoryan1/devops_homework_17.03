import os
var = os.getenv("hash")
with open('docker-compose.yml', 'r+') as f:
    lines = f.readlines()
    lines[3] = (lines[3])[:33] + str(var) + "\n"
    f.seek(0)
    for line in lines:
        f.write(line)
        print(lines[3])
