from xml.dom.minidom import parse
import xml.dom.minidom

def zmienTag(node, tekst):
    if node.firstChild.nodeType != node.TEXT_NODE:
        raise Exception("Node does not contain text")
    node.firstChild.replaceWholeText(tekst)

books = xml.dom.minidom.parse('books.xml')
print("--XML ma postać:")
print(books.toxml())

books_library = books.getElementsByTagName("book")
for book in books_library:
    print("--Book details--")
    title = book.getElementsByTagName('title')[0]
    print('Title: {}'.format(title.childNodes[0].data))
    country = book.getElementsByTagName('author')[0]
    print('Author: {}'.format(country.childNodes[0].data))
    year = book.getElementsByTagName('year')[0]
    print('Year: {}'.format(year.childNodes[0].data))
    test_tag = book.getElementsByTagName('test_tag')[0]
    print('Test_tag: {}'.format(test_tag.childNodes[0].data))

    zmienTag(test_tag, "zmieniam tag")

file_handle = open('books.xml', 'w')
books.writexml(file_handle)
file_handle.close()
