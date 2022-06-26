From kivymd.uix.screen from operator import truediv
from tkinter import CENTER, Menu
from turtle import color, setworldcoordinates
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
MDSeperator:
size_hint_:None
height: 12
MDBoxLayout:
adaptive_width:True
padding:  10
height:200

ScrollView:
size_hint_y:None
height:"190dp"
bar_width: 0

MDBoxLayout:
adaptive_width:True
spacing: 100

MDRelativeLayout:
md_bg_color: 1,1,1,1
size_hint_y:None
size:"110dp","190"

MDRelativeLayout:
md_bg_color: get color_from hex("Bebeb")
radius: 15
pos_hint{:"top:1",left:"1"}

FitImage:
source: root.profile_pic
radius:[15,15,0,0];
mipmap: True;
size_hint: None,None
size: "100dpx"
pos_hint:{"top:1","left:1"}

FitImage:
source:
pos_hint{'center: x0.5',center:y:0.35}
size_hint:None,None
MDLabel:
text:"Create Story"
theme_text_color:"Custom"
text_color:0,0,0,1;
halign:'center'
font_size:14
adaptive_height:True

MDBoxLayout:
adaptive_wight: True
id: stories

MDSeperator:
size_hint_y:None
height: 12



TwoLineAvatarIconListItem:
texxt:root.name
secondart_text: root.update
divider:None
_no_ripple_effect:True

ImageLeftWidget:
source: root.avatat
radius:[20,]

MDIconButton:
icon:"dots-hor"

























