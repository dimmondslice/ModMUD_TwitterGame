#Handles image generation. Takes in a list of strings(tweets). returns image.

from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap

def gen(messages, title = ""):

    lines = [title.center(42,"-")]
    for message in messages:
        wrappedmessage = wrap(message, width=40)
        for line in wrappedmessage:
            lines.append(" " + line)
        lines.append(" ")

    lines.append(" >_")
    lines.append("------------------------------------------")

    image = Image.new("RGBA", (770,int(27 * len(lines))), (0,20,0))

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("resources/MorePerfectDOSVGA.ttf", 32)
    text = "\n".join(line for line in lines)

    draw.text((8, 4), text, (0,255,0), font=font)

    #save image locally to test
    #image.save("test2.png")

    #return image
    return image
