from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
for a in os.listdir('.'):
    if a.endswith('.jpg'):
        img = Image.open(a)
        fn, flext = os.path.splitext(a)

        img= img.convert("L")
        img1 = img.filter(ImageFilter.DETAIL)
        img2 = img1.resize((1080, 1080))
        width, height = img2.size

        draw = ImageDraw.Draw(img2)
        text = "ZhetiSeven Studio"
        title = "BLACK"
        font = ImageFont.truetype("arial.ttf", 80)
        textwidth, textheight = draw.textsize(text, font)
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin
        draw.text((x, y), text, title, font=font)
        img2.save('Adil/{}{}'.format(fn, flext))
