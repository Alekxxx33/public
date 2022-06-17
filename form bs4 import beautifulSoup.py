form bs4 import beautifulSoup

with open('home.html','r')
as html file:

soup = BeautifulSoup(content,'hxml')
cours_cards = soup.find_all('div',class='card')
for course in cours_cards:
    course_nme = course.h5.text
    course_price = course.a.text.split()[-1]
]
print(f'{c} costs{course_price}')
    print(course_name)
    print(course_price)