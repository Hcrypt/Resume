import socket as sockMod
import urllib2

target = raw_input("Please enter an IP to be scanned: ")
print target+" will be scanning port 80."
print "If this information is correct, press enter to begin scanning."
cont = raw_input("Continue: ")
print "Scanning..."

website = target[target.find('') : target.find('.')]					# grabs the substring from the actual string

sox = sockMod.socket(sockMod.AF_INET, sockMod.SOCK_STREAM)
port = int(80)
saved_as_html = open(website + '.html', 'w')                # data of the actual website
saved_as_txt = open(website + '.txt', 'w')                  # metadata of the website saved as a text file

resCode = sox.connect_ex((target, port))

if resCode == 0:
    print "Port :: "+str(port)+" OPEN."

    if int(port) == 80:
            urlTarg = ("http://"+target+"/")
            page = urllib2.urlopen(urlTarg)
	# Read the referenced/opened web page into the html object as string data.
            html = page.read()
	# Use string slicing and the find methods to cut out the title of the web page.
            title = html[html.find("<title>")+7:html.find("</title>")]
            print "+"*60
            print title
            print "+"*60
##            pageinfo = page.info()
##            print pageinfo
            print "+"*60
    # Tear down the socket before we try opening another.
    sox.close()

pageinfo = page.info()          # pageinfo is the variable holding all the information in page.info()
# print (type(pageinfo))
pageinfo = str(pageinfo)        # the datatype of pageinfo is a "instance" data type and so I need to convert it to a string
print pageinfo
#print (type(pageinfo))         # double checked to see if it's a string data type

saved_as_html.write(html)       # everything under "html" is output into the variable "saved_as_html"
saved_as_txt.write(pageinfo)       # everything under "html" is output into the variable "saved_as_html"

# Cosmetic information, then "pause" so the user can review the information in the terminal.
print "Scanning complete."
con = raw_input("Press enter to finish: ")
