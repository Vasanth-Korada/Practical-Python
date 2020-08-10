from PIL import Image,ImageDraw,ImageFont

img = Image.new(mode="RGB",size=(600,100),color="orange")

draw = ImageDraw.Draw(img)

fnt = ImageFont.truetype("arial.ttf",size=32)

draw.text(xy=(220,35),text="INFY TECH",size=32,font=fnt)


img.show("test.png")

