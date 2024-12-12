import argparse
import requests

def download(url,filename):
    # if filename =="None":
    if filename is None:
        filename=url.split("/")[-1]
        print(filename)
    with requests.get(url,stream=True) as r:
        r.raise_for_status()
        with open(filename,"wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return filename 
parser=argparse.ArgumentParser()
#Add command line arguments
parser.add_argument("examples",help="ye description hai")
parser.add_argument("-o","--output",help="Description 2")
#Prase the arguments
args=parser.parse_args()

#Use the arguments in your code
print(args.examples)
print(args.output)
print(type(args.examples))
print(type(args.output))
download(args.examples,args.output)