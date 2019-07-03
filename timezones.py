import datetime as dt
import dateutil.parser

clients = {}

with open("times.txt") as f:
    tday = dt.datetime.now(dt.timezone.utc)
    print("Current server time(UTC):")
    print(tday)

    for line in f:
        index, time = line.split()
        clients[index] = dateutil.parser.parse(time) - tday

    sortedClients = sorted(clients.items(), key=lambda x: x[1])
    
    print("\nOrdered clients:")
    print("Client     Date       Time+timezone")
    for client in sortedClients:
        print('client ' + client[0] + ' : ' + str(client[1] + tday))
