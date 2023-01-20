import re , argparse

parser = argparse.ArgumentParser(description='parse burp suite site map and extraxt urls')
parser.add_argument('-i', '--input', type=str, help='sitemap xml file: google.xml')
parser.add_argument('-o', '--output', type=str, help='outputfile: burp_urls.txt' , default='burp_urls.txt')
parser.add_argument('-c', '--cli', type=str, help='to print all url in cli, dont save output in file.')
args = parser.parse_args()


path = args.input
out = args.output
cli = args.cli




#input
file = open(path,"r")
burpfile = file.read()
file.close()


def get_url(xmlfile):
    #get all url elemet value and pull in the list 
    regex = r"<url><\!\[CDATA\[(.+?)\]\]"
    path = re.findall(regex, xmlfile)
    #return a list of path
    return path

all = get_url(burpfile)

if cli:
    for i in all:
        print(i)
else:
    #output
    outfile = open(out,"w+")
    for i in all:
        outfile.write(i+'\n')
    outfile.close()
    print(f"Ok all url saved in {out} file")
