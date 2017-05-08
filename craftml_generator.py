from PIL import Image
import sys

def colorF(decVal):
    hexVal = '%x' % decVal
    if len(hexVal) == 1:
        hexVal = '0{}'.format(hexVal)
    return hexVal

def main(argv):
    if len(sys.argv) != 3:
        print "USAGE: python craftml_generator.py <DOWNSCALE> <FILE NAME>"

    downscale = int(sys.argv[1])
    f = open("output.html", "w")

    img = Image.open(sys.argv[2])
    imgcp = img.copy()

    size = img.width/downscale, img.height/downscale
    imgcp.thumbnail(size)

    img.close()

    for x in range(0, imgcp.width):
        for y in range(0, imgcp.height):
            r, g, b = imgcp.getpixel((x, y))

            f.write('<cube size="1 1 1" t="translate {x} {y} 1" style="color: #{r}{g}{b}"></cube>\n'.format(x=x, y=y, r=colorF(r), g=colorF(g), b=colorF(b)))

    f.close()

main(sys.argv)
