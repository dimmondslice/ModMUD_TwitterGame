#Handles image generation. Takes in a list of strings(tweets). returns image.

from PIL import Image, ImageDraw, ImageFont

def gen(messages, title = ""):

    lines = [title.center(50,"-")]
    for message in messages:
        while(True):
            if len(message) <= 48:
                lines.append(" " + message)
                lines.append(" ")
                break
            else:
                lines.append(" " + message[:48])
                message = message[48:]
    lines.append("--------------------------------------------------")

    image = Image.new("RGBA", (916,int(27 * len(lines))), (0,20,0))

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("resources/MorePerfectDOSVGA.ttf", 32)
    text = "\n".join(line for line in lines)

    draw.text((8, 4), text, (0,255,0), font=font)

    #save image locally to test
    #image.save("test.png")

    return image

