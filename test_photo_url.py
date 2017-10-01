from PIL import Image
import os
import urllib, cStringIO
import io
import subprocess
import argparse
from flask import Flask, request

#def getPhotoFromURL(URL):
#    file = cStringIO.StringIO(urllib.urlopen(URL).read())
#    image = Image.open(file)
#    image.save("urlPhoto.jpg", "JPEG")

#    proc = subprocess.Popen('bazel build tensorflow/examples/image_retraining:label_image && bazel-bin/tensorflow/examples/image_retraining/label_image --graph=/tmp/output_graph.pb --labels=/tmp/output_labels.txt --output_layer=final_result:0 --image=urlPhoto.jpg', shell=True, stdout=subprocess.PIPE)
#    tmp = proc.stdout.read()
#    #return parsedTMP
#    return tmp.split("(", 1)[0]

app = Flask(__name__)
@app.route('/classify')

#parser = argparse.ArgumentParser(description="Get url from command")
#parser.add_argument('--URL', action="store", dest='URL', default=0)
#args = parser.parse_args()
#getPhotoFromURL(str(args.URL))

#app.getPhotoFromURL(URL)

def classify():
    file = cStringIO.StringIO(urllib.urlopen("http://storage.googleapis.com/recycleanse/image.png").read())
    image = Image.open(file)
    image.save("urlPhoto.jpg", "JPEG")

    proc = subprocess.Popen('bazel build tensorflow/examples/image_retraining:label_image && bazel-bin/tensorflow/examples/image_retraining/label_image --graph=/tmp/output_graph.pb --labels=/tmp/output_labels.txt --output_layer=final_result:0 --image=urlPhoto.jpg', shell=True, stdout=subprocess.PIPE)
    tmp = proc.stdout.read()
    #return parsedTMP
    tmp = tmp.split("(", 1)[0]
    return tmp
