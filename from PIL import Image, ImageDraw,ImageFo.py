from PIL import Image, ImageDraw,ImageFont 
import textwrap
im= Image.open("./idontalways.jpg")
draw=Image.Draw(im)
image_width,image_height= im.size
font= ImageFont.truetypr(font="./fonts/impact/impact.ttf", size=int(image_height/12))
top_text="I dont alwats make memes"
bottom_text= "Bit when I do,I use Python"
top_text= top_text.upper()
bottom_text= bottom_text.upper()
char_width,char_height= font.gets.size('a')
chars_perline= image_width// char_width
top_lines= textwrap.(top_text, width=chars_per_line)
bottom_lines- textwrap.wrap(bottom_text, width-chars_per-line)
bottom_lines
{'BUt WHEN I DO I'.'USE PYTHoN'}