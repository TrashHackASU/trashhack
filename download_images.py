import urllib
import sys  

##reload(sys)  
##sys.setdefaultencoding('utf8')

images_link = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04557648"
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
