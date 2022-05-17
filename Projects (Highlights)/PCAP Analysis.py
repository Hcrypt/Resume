import dpkt                     # Import dpkt module used for parsing captured files.
import socket                   # Import socket module containing a ton of resources dealing with network data, performing network tasks..etc

# Grabs pcap file and opens it.
capFile = open('SkypeIRC.cap', 'rb')
# Reads captured file into pcapObject which is prepared and ready for processing using/with the dpkt module
f = open('./vangbe_pcap_analysis.csv', 'w')

pcapObject = dpkt.pcap.Reader(capFile)

# pcapObject is iterable, each packet in the object can be iterated through and accessed through it.
for timestamp, rawPacketData in pcapObject:                                     # For every time pcapObject is looped, look through the timestamp, rawPacketData in pcapObject
	ethernetData = dpkt.ethernet.Ethernet(rawPacketData)                    # Use the dpkt module to read only the raw Ethernet packet data from pcapObject.
	ipBinary = ethernetData.data                                            # Used to parse more data from the eternetData object into the ipBinary object
	try:                                                                    # We expect their might be errors, therefore we create the try/except error handling.
		destIP = socket.inet_ntoa(ipBinary.dst)                         # Grabs destination ip from ipbinary object
		srcIP = socket.inet_ntoa(ipBinary.src)                          # Grabs source ip from ipbinary object
                print ("[ + ]  Total pwnage timestampt: "+str(timestamp))
                print ("[ + ]  Total pwnage target: "+destIP)
                print ("[ + ]  Total pwning box:    "+srcIP)
                print (":) "*20)                                                # prints ":) " about 20 times
                f.write (str(timestamp)+ "," + destIP + "," + srcIP + "\r")     # write timestamp, destination and source ip information into csv file
	except AttributeError:                                                  # Anything under except is INCASE their is an error
		print "ERROR DECODING IP"
	except socket.error:
		print "ERROR DECODING IP"
end = raw_input("Press enter to finish: ")                                      # To create a pause in the program
