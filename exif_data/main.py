import PIL.Image
import PIL.ExifTags
import optparse
import os
import pprint

def check_path(path : str) -> None:
    new_path = os.path.abspath(path)
    if not os.path.isfile(new_path):
        print("[-] Inccorrect path")
        exit()
    
def get_argumnets() -> dict:
    parser = optparse.OptionParser()
    parser.add_option("-p","--path",dest="path",help="Please enter path to image")
    arguments = parser.parse_args()[0]
    if not arguments.path:
        parser.error("Use -p, for more information --help")
    check_path(arguments.path)
    arguments.path = os.path.abspath(arguments.path)
    return arguments

def exif_func(path : str) ->None:
    img = PIL.Image.open(path)
    exif = {PIL.ExifTags.TAGS[k] : v for k,v in img._getexif().items() if k in PIL.ExifTags.TAGS}
    pprint.pprint(exif , indent=4)
   
exif_func(get_argumnets().path)