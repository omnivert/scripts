from bs4 import BeautifulSoup

# make something that downloads html pages
# for now we have a test html file
fname = 'test.html'
with open(fname) as fp:
    soup = BeautifulSoup(fp, 'html.parser')

print(soup.name)
print(soup('a'))
