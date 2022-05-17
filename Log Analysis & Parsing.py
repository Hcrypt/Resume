
fileObj = open('firewall_log.log', 'r')

listObj = fileObj.readlines()

newFileObj = open('VangBee_Lab03.txt', 'w')
newCSVFileObj = open('VangBee_Lab03.csv', 'w')

for line in listObj:
    oip = line[line.find('Source:') : line.find(' - D')]
    dip = line[line.find('Destination:') : line.rfind('[Drop]')]
    date_time = line[0 : line.find(' - ')]
    event = line[line.rfind("["): line.rfind(']') +1]

#    print (oip)    
#    print ('Original IP Address: ' + oip + ' From ' + dip + ' Date and Time: ' + date_time + ' Event: ' + event \n\r')

    newFileObj.write('Original IP Address: ' + oip + ' From ' + dip + ' Date and Time: ' + date_time + ' Event: ' + event + '\n\r')
    newCSVFileObj.write (oip + dip + date_time + event + '\r')

fileObj.close()
