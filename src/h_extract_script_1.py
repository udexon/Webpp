from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
a=soup
[x.extract() for x in a.findAll('script')]
s.append(str(a))
f('_/a.html wl:')
