import argparse
import tempfile
import zipfile
from shutil import copyfile 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="the file name to be processed")
    parser.add_argument("xml", help="the file name to be processed")
    parser.add_argument("dst", help="the file name to be processed")
        
    args = parser.parse_args()
            
    temporaryFolder = tempfile.mkdtemp()
    temporaryZipFile = temporaryFolder+'/temp.zip'
    # copy the file to a temporary file with .zip ending 
    copyfile(args.src, temporaryZipFile)
    
    with zipfile.ZipFile(temporaryZipFile, 'r') as z:
        z.extractall(temporaryFolder)
    
    extractedXmlFile = temporaryFolder+'/word/' + args.xml
    
    copyfile(extractedXmlFile, args.dst)
    print(args.dst)
