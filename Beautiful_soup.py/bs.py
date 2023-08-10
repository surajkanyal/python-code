from bs4 import BeautifulSoup
# import lxml  if html parser dont work you can try other parser
with open('/home/suraj/Desktop/python/Beautiful_soup.py/website.html') as file:
    contents = file.read() 

soup = BeautifulSoup(contents,'html.parser')
# content and parser

# print(soup.title)  # give the title tag
# print(soup.title.string) #gives the title name
# print(soup.prettify())  #prettifies messed up code

# # Now how to find

# #find_all
# #take use of tags
# all_anchor_tag = soup.find_all(name = 'a')
# print(all_anchor_tag)
# # or if you need only data
# for a in all_anchor_tag:
#     print(a.getText())

# # if we need only links or other in other tags
# for tag in all_anchor_tag:
#     print(tag.get('href'))  # use method get to get the specific attribute value


# we can also search by attribute name
#FIND  # it will give me the earkiest occurence of that
heading =soup.find(name ='h1',id = 'name')
print(heading)

# finding class
section_head = soup.find(name = 'h3',class_='heading') # class is reserved keyword therefore use '_'

print(section_head.name)