import csv

def airport(icao):
    csv_file = csv.reader(open('./icao_iata.csv', 'r'))

    #find the value in the relevant csv and return an IATA code
    for row in csv_file:
        if icao in row[0]:
            iata = ''.join(row)
            iata = iata[5:8]
            print(iata)
    return iata