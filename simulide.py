from lxml import etree as ET
import os


class Component():
    def __init__(self, name, inputs, outputs, wires, statements):        
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.wires = wires
        self.statements = statements
        os.mkdir(f'./{name}')


    def create_package(self):
        # root element
        packageB = ET.Element("packageB", 
                              name="Package", 
                              width="8", 
                              height=f"{max(len(self.inputs), len(self.outputs)) + 1}", 
                              background="", 
                              type="None")

        for index, value in enumerate(self.inputs):     # inputs
            pin = ET.SubElement(packageB, "pin", 
                                type="",
                                xpos="-8",
                                ypos=f"{8+(index*8)}",
                                angle="180",
                                length="8",  
                                space="0",   
                                id=f"{value}",     
                                label=f"{value}")

        for index, value in enumerate(self.outputs):     # outputs
            pin = ET.SubElement(packageB, "pin", 
                                type="",
                                xpos="72",
                                ypos=f"{8+(index*8)}",
                                angle="0",
                                length="8",  
                                space="0",   
                                id=f"{value}",     
                                label=f"{value}")


        # elements tree
        tree = ET.ElementTree(packageB)

        # file's header and content
        with open(f"./{self.name}/{self.name}.package", "wb") as f:
            f.write(b'<!DOCTYPE SimulIDE>\n\n')
            f.write(b'<!-- This file was generated by veri2sim -->\n\n')
            tree.write(f, encoding="utf-8", xml_declaration=False, pretty_print=True)

    def create_mcu(self):
        # root element
        iou = ET.Element("iou", 
                         name=f"{self.name}", 
                         core="scripted", 
                         script=f"{self.name}.as")

        # inputs
        ioport = ET.SubElement(iou, "ioport", 
                               name="InputPort", 
                               pins=",".join(self.inputs))
        
        # outputs
        ioport = ET.SubElement(iou, "ioport", 
                               name="OutputPort", 
                               pins=",".join(self.outputs))
        
        # element tree
        tree = ET.ElementTree(iou)

        # file's header and content
        with open(f"./{self.name}/{self.name}.mcu", "wb") as f:
            f.write(b'<!DOCTYPE SimulIDE>\n\n')
            f.write(b'<!-- This file was generated by veri2sim -->\n\n')
            tree.write(f, encoding="utf-8", xml_declaration=False, pretty_print=True)

    def create_script(self):
        with open(f"./{self.name}/{self.name}.as", "w") as f:
            # inputs and outputs
            for input in self.inputs:
                f.write(f'IoPin@ {input}Pin = component.getPin("{input}");\n')
            for output in self.outputs:
                f.write(f'IoPin@ {output}Pin = component.getPin("{output}");\n')

            # global variables and functions
            f.write('\n// ___global_definitions___')
            for wire in self.wires:
                f.write(f'\ndouble {wire} = 0.0;')


            # setup function
            f.write(f'\n\nvoid setup()\n{{\n\tprint("{self.name} setup()");\n}}')
            
            # reset function
            f.write(f'\n\nvoid reset()\n{{\n\tprint("{self.name} reset()");\n\n')
            for input in self.inputs:
                f.write(f'\t{input}Pin.setPinMode( 1 ); // Input\n')
            for output in self.outputs:
                f.write(f'\t{output}Pin.setPinMode( 3 ); // Output\n')
            f.write('\n')    
            for input in self.inputs:
                f.write(f'\t{input}Pin.changeCallBack( element, true );\n')
            f.write('\n')
            for output in self.outputs:
                f.write(f'\t{output}Pin.setVoltage( 0 );\n')
            f.write('}\n')

            # voltChanged function
            f.write('\nvoid voltChanged()\n{\n\t// ___implementation___\n')
            for statement in self.statements:
                if statement[0] == 'assign':
                    if statement[1] in self.outputs: #outputs
                        if statement[2] in self.inputs: # output <= input
                            f.write(f'\t{statement[1]}Pin.setVoltage( {statement[2]}Pin.getVoltage() );\n')
                        else:                           # output <= statement
                            f.write(f'\t{statement[1]}Pin.setVoltage( {statement[2]} );\n')
                    else:   #wires
                        if statement[2] in self.inputs: # wire <= input
                            f.write(f'\t{statement[1]} = {statement[2]}Pin.getVoltage();\n')
                        else:                           # wire <= statement
                            f.write(f'\t{statement[1]} = {statement[2]};\n') 
            f.write('}\n')
