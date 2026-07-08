import argparse
import requests
parser=argparse.ArgumentParser()




def download_file(url,local_filename):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                
                f.write(chunk)
    return local_filename

#Add command line Arguments
parser.add_argument("url",help="url of the file to download")
parser.add_argument("output",help="by which name do you want to save your file")

#Parse the arguments
args=parser.parse_args()

print(args.url)
print(args.output)
download_file(args.url,args.output)