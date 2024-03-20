import os
var = os.getenv("hash")
with open('docker-compose.yml', 'r+') as f:
    lines = f.readlines()
    lines[11] = (lines[11])[:32] + str(var) + "\n"
    f.seek(0)
    for line in lines:
        f.write(line)
        print(lines[11])
