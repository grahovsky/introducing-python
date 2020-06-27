import xml.etree.ElementTree as et
tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
print(root.tag)

for child in root:
    print('tag:', child.tag, 'attributes:', child.attrib, 'text:', child.text)
    for grandchild in child:
        print('\t tag:', grandchild.tag, 'attributes:', grandchild.attrib, 'text:', grandchild.text)

# find by attributes
pancakes = root.findall('./breakfast/item[@price="$4.00"]')[0]
print('tag:', pancakes.tag, 'attributes:', pancakes.attrib, 'text:', pancakes.text)

# Other standard Python XML libraries include the following:
#
# xml.dom
# The Document Object Model (DOM), familiar to JavaScript developers, represents web documents as hierarchical structures. This module loads the entire XML file into memory and lets you access all the pieces equally.
#
# xml.sax
# Simple API for XML, or SAX, parses XML on the fly, so it does not have to load everything into memory at once. Therefore, it can be a good choice if you need to process very large streams of XML.
