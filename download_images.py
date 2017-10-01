import urllib
import sys
import os

##reload(sys)
##sys.setdefaultencoding('utf8')
def scrapeImages(url, myPath, start):
    images_link = url
    images_url = urllib.urlopen(images_link).read()
    pic_num = start

    for i in images_url.split('\n')[start:]:
        try:
            print(i)

            try:
                r = urllib.urlopen(i).getcode()
            except IOError:
                print "error opening " + str(i)
                continue

            print r
            if r == 200:
                fullfilename = os.path.join(myPath, str(pic_num)+".jpg")
                urllib.urlretrieve(i, fullfilename)
                pic_num += 1

        except KeyboardInterrupt:
            print "Closing"
            break


URL = ""
Path_to_Folder = ""
Start_Index = 3

scrapeImages(URL, Path_to_Folder, Start_Index)
