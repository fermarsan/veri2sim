from lxml import etree as ET


class package():
    def __init__(self, name, inputs, outputs):        
        self.name = name
        self.inputs = inputs
        self.outputs = outputs

    def create():
        packageB = ET.Element("packageB")

        for index, value in enumerate(self.inputs):
            pin = ET.SubElement(packageB, "pin", 
                                param1=f"p{index}1", 
                                param2=f"p{index}2")


        # Crear un árbol de elementos
        tree = ET.ElementTree(packageB)

        # Escribir el árbol en un archivo XML con DOCTYPE
        with open("{self.name}.package", "wb") as f:
            f.write(b'<!DOCTYPE SimulIDE">\n\n')
            f.write(b'<!-- This file was generated by veri2sim -->\n\n')
            tree.write(f, encoding="utf-8", xml_declaration=False, pretty_print=True)