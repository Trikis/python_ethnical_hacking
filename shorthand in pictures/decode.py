from PIL import Image
import optparse
import os

def get_arguments() -> str:
    parser = optparse.OptionParser()
    parser.add_option("-p","--path",dest="path",help="Path to encoded image with message")
    arguments = parser.parse_args()[0]
    if not arguments.path:
        parser.error("Use -p option, for more information use --help")
    
    arguments.path = os.path.abspath(arguments.path)
    if not os.path.isfile(arguments.path):
        print("[-] Incorrect path")
        exit()
    return arguments.path

def decode() -> None:
    path = get_arguments()
    new_array =[]
    d_image = Image.open(path)
    out_image = Image.new('1',d_image.size)
    width, height = d_image.size

    for h in range(height):
        for w in range(width):
            d_pixel = d_image.getpixel((w,h))
            if d_pixel[2] & 1 == 0:
                out_pixel = 0
            else:
                out_pixel = 1
            new_array.append(out_pixel)
    out_image.putdata(new_array)
    out_image.show()


decode()