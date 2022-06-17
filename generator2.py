Imports in[1]:
from cgitb import text
from mailbox import linesep
from PIL import Image,ImageDraw,ImageFont
import textwrap
Load image
In[]:im= Image.open("./idontalways.jpg")
In [3]: draw=ImageDraw.Draw(im)
in[4]:image_width,image_height= im.size

Load font
In[]: font= ImageFont.truetype(font="/,impact/imact.tft",size=int(image_height/10))


Wrap textIn[]: top_text="I dont always make memes"
bottom_text = But when I do .I use Python" 
In[]:top_text= top_text.upper()
bottom_text

In[7]: char_width, char_height= font.getsize('A')
In[]: vhars_per_line= image_width / char_width
top_lines- textwrap.wrap(top_text,width=chars_per_line)

top_lines- textwrap.wrap(top_text,width=chars_per_line)
bottom_lines- textwrap.wrap(top_text,width=chars_per_line)
in[12]: bottom_lines
Out[12]:[I dont alwats','make memes']

Draw lines
In[]: y = 10
for line in top_lines:
    line_width,line_height= font.getsize()
    x = (image_widtg - line width)/2
    draw.text(x,y),line, fill-height='white',font= font)
    In[30]: im.show()
    y += line_height
    In[]: y=image_heightchar_height * len(bottom_lines)
    In[24]: im.show()