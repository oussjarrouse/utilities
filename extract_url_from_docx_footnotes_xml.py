import argparse
import xml.etree.ElementTree as ET
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="the file name to be processed")
    parser.add_argument("dst", help="the file name to be processed")
    args = parser.parse_args()
    # Do stuff to the docx file to extract the footnotes.xml
    footnoteXmlFile = args.src
    tree = ET.parse(footnoteXmlFile)
    urls = list()
    for node in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hyperlink'):
        for n in node.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
            urls.append(n.text)
    
    thefile = open(args.dst, 'w')
    counter = 0        
    for url in urls:
        counter+=1
        thefile.write("%s\n" % url)
        
    thefile.close()
