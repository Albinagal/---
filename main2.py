with open("var.txt", "r") as f:
    s = f.read()
s = s[1:-1:].split(",")

thingId = s[0].split()[1][1:-1:]
type = s[1].split()[1][1:-1:]
timeStamp = s[2].split()[1]
hwVer = s[3].split()[1][1:-1:]
swVer = s[4].split()[1][1:-1:]
contractVer = s[5].split()[1][1:-1:]
a = s[6] + s[7] + s[8] + s[9]
current = [float(a.split("{")[2].split()[1]), float(a.split("{")[2].split()[3][:-1:])]
isWatering = s[10].split()[1]
isWorking = s[11].split()[1]

