import urllib
import sys

##reload(sys)
##sys.setdefaultencoding('utf8')
def scrapeImages(url):
    images_link = url
    images_url = urllib.urlopen(images_link).read()
    pic_num = 1

    for i in images_url.split('\n'):
        try:
            print(i)

            try:
                r = urllib.urlopen(i).getcode()
            except IOError:
                print "error opening " + str(i)
                continue

            print r
            if r == 200:
                urllib.urlretrieve(i, str(pic_num)+".jpg")
                pic_num += 1

        except KeyboardInterrupt:
            print "Closing"
            break

scrapeImages("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04255586")
