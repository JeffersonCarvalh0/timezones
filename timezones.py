import datetime as dt
import dateutil.parser

clients = {}

with open("times.txt") as f:
    tday = dt.datetime.now(dt.timezone.utc)

    for line in f:
        index, time = line.split()
        clients[index] = dateutil.parser.parse(time) - tday

    sortedClients = sorted(clients.items(), key=lambda x: x[1])
    
    for client in sortedClients:
        print(client)
