import xml.etree.ElementTree as ET
from xml.dom import minidom

class Carga_archivo:

    def archivoCarga(self, link):
        print(link)

        #try:
        tree=ET.parse(link)
        #self.rootM=tree.getroot()
        
        #print(tree)