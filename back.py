import os
var = os.getenv("hash")
with open('docker-compose.yml', 'r+') as f:
    lines = f.readlines()
    index = lines[11].find(":", 15]
    lines[11] = (lines[11])[:index+1] + str(var) + "\n"
    f.seek(0)
    for line in lines:
        f.write(line)
        print(lines[11])
