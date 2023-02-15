"""Program that prints number of tags in an xml file and
prints individual elements of the file"""

import xml.etree.ElementTree as ET
input = """<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>"""

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('user count:', len(lst))
for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attribute:', item.get("x"))
"""Program that prints number of tags in an xml file and
prints individual elements of the file"""

