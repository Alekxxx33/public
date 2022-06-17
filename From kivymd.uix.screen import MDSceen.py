From kivymd.uix.screen from operator import truediv
from tkinter import Menu
from xml.etree.ElementTree import TreeBuilder
import MDSceen

class_HomePage()

<HomePage>
MDBoxLayout:
orientation:'vertical'

MDToolbar:
md_bg_color:1,1,1,1
title:'facebook'
specific_text_color:get_color_from_hex()
right_Action_iems:[[|''],["facebook-messenger"]]
MDBoxLayout:
adaptive_size: True
height:30
spacing:25

MDIconButton:
icon:"home"
MDIconButton:
icon:"account-circle-outline"
MDIconButton:
icon:"account-group-line-outline"
MDIconButton:
icon:"bell-outline"
MDIconButton:
Menu
MDBoxLayout:
ScrollView:
bar_width: 0
MDBoxLayout:
adaptive_height:true

MDBoxLayout:
adaptive_height: True
orientation:ventical
id:timeline
MdSeperator:
MDBoxLayout:
orientation:"horizontial"
height:100

AvatarImage:
source: root.profile_pic
MDRoundFlatIconButton:
text:"Write something here/nWriteSomething here"
size_hint:1,1
line_color:0,0,0,1:
text_color:0,0,0,1:

MdSeperator

MDBoxLayout:

ThreeButons:
text:"live"
icon:"video"
icon_color:get_color_from_hex('#F2')

MDSeperator:
size_hint_x: None;
width:1:
height:1:

MDSeperator:
size_hint_y: None
height:70
bar_width:0
MDBoxLayout:
adaptive_width:Truespacing:10
padding:10
MDRoundFlatIconButton:
text:"Create/nRoom"
icon:"video-plus"
pos_hint:"\center-x:0.5;'center_y:0.5"

MDBoxLayout:
adaptive_wight:true;
id:online_friends;
padding: 10
spacing: 10