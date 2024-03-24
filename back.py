import os
var = os.getenv("hash")
with open('docker-compose.yml', 'r+') as f:
    lines = f.readlines()
    index = lines[12].find(":", 10)
    lines[12] = (lines[12])[:index+1] + str(var) + "\n"
    f.seek(0)
    for line in lines:
        f.write(line)
        print(lines[12])
