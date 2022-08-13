from PIL import Image
import optparse
import os

def get_arguments() -> dict:
    parser = optparse.OptionParser()
    parser.add_option("-s","--sourse", dest ="sourse" , help="The sourse, where the message will be inserted")
    parser.add_option("-m", "--message" , dest ="message", help="Message which will be hidden in the sourse")
    arguments = parser.parse_args()[0]
    if not arguments.sourse:
        parser.error("Use option -s , for more information use --help")
    elif not arguments.message:
        parser.error("Use option -m , for more information use --help")
    arguments.sourse = os.path.abspath(arguments.sourse)
    arguments.message = os.path.abspath(arguments.message)
    if not os.path.isfile(arguments.sourse):
        print("[-] Inccorect path of sourse image")
        exit()
    elif not os.path.isfile(arguments.message):
        print("[-] Incorrect path of message image")
        exit()
    return arguments

def convert() -> None:
    arguments = get_arguments()
    c_image = Image.open(arguments.sourse)
    m_image = Image.open(arguments.message)

    m_image = m_image.resize(c_image.size).convert('1')
    out_image = Image.new('RGB',c_image.size)
    new_array =[]
    width , height = c_image.size

    for h in range(height):
        for w in range(width):
            c_pixel = c_image.getpixel((w,h))
            m_pixel = m_image.getpixel((w,h))
            if m_pixel == 0:
                new_blue_pixel = c_pixel[2] & 254
            else:
                new_blue_pixel = c_pixel[2] | 1
            new_array.append((c_pixel[0] , c_pixel[1] , new_blue_pixel)) 

    out_image.putdata(new_array)
    path = os.path.join('encoded','encoded_message.png')
    out_image.save(path)


convert()