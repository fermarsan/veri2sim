from lxml import etree as ET
import os


class Component():
    def __init__(self, name, symbols, statements):        
        self.name = name
        self.symbols = symbols
        self.statements = statements
        os.makedirs(f'./output/{name}', exist_ok=True)

    def single_inputs(self):
        counter = 0
        for symbol in self.symbols:
            msb = self.symbols[symbol].msb 
            lsb = self.symbols[symbol].lsb 
            if self.symbols[symbol].type == 'input':
                if msb == lsb:                  # single input
                    counter += 1
                else:
                    counter += (msb - lsb) + 1  # input array
        return counter

    def single_outputs(self):
        counter = 0
        for symbol in self.symbols:
            msb = self.symbols[symbol].msb 
            lsb = self.symbols[symbol].lsb 
            if type == 'output':
                if msb == lsb:                  # single output
                    counter += 1
                else:
                    counter += (msb - lsb) + 1  # output array
        return counter

    def create_package(self):
        # root element
        packageB = ET.Element("packageB", 
                              name="Package", 
                              width="8", 
                              height=f"{max(self.single_inputs(), self.single_outputs()) + 1}", 
                              background="", 
                              type="None")

        # -------------------- inputs --------------------
        i = 0
        for symbol in self.symbols:
            msb = self.symbols[symbol].msb 
            lsb = self.symbols[symbol].lsb 
            if self.symbols[symbol].type == 'input':
                if msb == lsb:        # single input
                    pin = ET.SubElement(packageB, "pin", 
                                        type="",
                                        xpos="-8",
                                        ypos=f"{8+(i*8)}",
                                        angle="180",
                                        length="8",  
                                        space="0",   
                                        id=f"{symbol}",     
                                        label=f"{symbol}")
                    i += 1
                else:                               # input array
                    for j in range(lsb, msb+1):
                        pin = ET.SubElement(packageB, "pin", 
                                            type="",
                                            xpos="-8",
                                            ypos=f"{8+(i*8)}",
                                            angle="180",
                                            length="8",  
                                            space="0",   
                                            id=f"{symbol}_{j}",     
                                            label=f"{symbol}_{j}")
                        i += 1

        # -------------------- outputs --------------------
        i = 0
        for symbol in self.symbols:
            msb = self.symbols[symbol].msb 
            lsb = self.symbols[symbol].lsb 
            if self.symbols[symbol].type == 'output':
                if msb == lsb:        # single output            
                    pin = ET.SubElement(packageB, "pin", 
                                        type="",
                                        xpos="72",
                                        ypos=f"{8+(i*8)}",
                                        angle="0",
                                        length="8",  
                                        space="0",   
                                        id=f"{symbol}",     
                                        label=f"{symbol}")
                    i += 1
                else:                               # output array
                    for j in range(lsb, msb+1):
                        pin = ET.SubElement(packageB, "pin", 
                                            type="",
                                            xpos="72",
                                            ypos=f"{8+(i*8)}",
                                            angle="0",
                                            length="8",  
                                            space="0",   
                                            id=f"{symbol}_{j}",     
                                            label=f"{symbol}_{j}")
                        i += 1

        # elements tree
        tree = ET.ElementTree(packageB)

        # file's header and content
        with open(f"./output/{self.name}/{self.name}.package", "wb") as f:
            f.write(b'<!DOCTYPE SimulIDE>\n\n')
            f.write(b'<!-- This file was generated by veri2sim -->\n\n')
            tree.write(f, encoding="utf-8", xml_declaration=False, pretty_print=True)

    def create_mcu(self):
        # root element
        iou = ET.Element("iou", 
                         name=f"{self.name}", 
                         core="scripted", 
                         script=f"{self.name}.as")

        # -------------------- single inputs/outputs --------------------
        pin_list = ''
        for symbol in self.symbols:
            type = self.symbols[symbol].type 
            msb = self.symbols[symbol].msb 
            lsb = self.symbols[symbol].lsb
            if type in ['input', 'output'] and msb == lsb: 
                pin_list += symbol + ','
        
        if pin_list != '':
            ioport = ET.SubElement(iou, "ioport", name="SinglePinsPort", pins=pin_list[:-1])
             
        # -------------------- pin array inputs/outputs --------------------
        for symbol in self.symbols:
            type = self.symbols[symbol].type 
            msb = self.symbols[symbol].msb 
            lsb = self.symbols[symbol].lsb 
            if type in ['input', 'output'] and msb != lsb:        # pin array
                ioport = ET.SubElement(iou, "ioport", 
                                       name=f"{symbol}Port", 
                                       pins=",".join([f"{symbol}_{i}" for i in range(lsb, msb+1)]))
        
        # element tree
        tree = ET.ElementTree(iou)

        # file's header and content
        with open(f"./output/{self.name}/{self.name}.mcu", "wb") as f:
            f.write(b'<!DOCTYPE SimulIDE>\n\n')
            f.write(b'<!-- This file was generated by veri2sim -->\n\n')
            tree.write(f, encoding="utf-8", xml_declaration=False, pretty_print=True)

    def create_script(self):
        with open(f"./output/{self.name}/{self.name}.as", "w") as f:
            f.write('// This file was generated by veri2sim\n\n')

            # -------------------- inputs and outputs --------------------
            for symbol in self.symbols:
                type = self.symbols[symbol].type 
                msb = self.symbols[symbol].msb 
                lsb = self.symbols[symbol].lsb
                if type in ['input', 'output']:
                    if msb == lsb: 
                        f.write(f'IoPin@ {symbol}Pin = component.getPin("{symbol}");\n')
                    else:
                        f.write(f'IoPort@ {symbol}Port = component.getPort("{symbol}Port");\n')

            # -------------------- global variables and functions --------------------
            f.write('\n// ___global_definitions___')
            for symbol in self.symbols:
                msb = self.symbols[symbol].msb 
                lsb = self.symbols[symbol].lsb
                if self.symbols[symbol].type == 'wire':
                    if msb == lsb: 
                        f.write(f'\nbool {symbol} = false;')
                    else:
                        f.write(f'\nuint {symbol} = 0;')

            # -------------------- setup function --------------------
            f.write(f'\n\nvoid setup()\n{{\n\tprint("{self.name} setup()");\n}}')
            
            # -------------------- reset function --------------------
            f.write(f'\n\nvoid reset()\n{{\n\tprint("{self.name} reset()");\n\n')
            for symbol in self.symbols:
                msb = self.symbols[symbol].msb 
                lsb = self.symbols[symbol].lsb
                if self.symbols[symbol].type == 'input':
                    if msb == lsb: 
                        f.write(f'\t{symbol}Pin.setPinMode(1); // Input\n')
                        f.write(f'\t{symbol}Pin.changeCallBack(element, true);\n')
                    else:
                        f.write(f'\t{symbol}Port.setPinMode(1); // Input\n')
                        f.write(f'\t{symbol}Port.changeCallBack(element, true);\n')
                elif self.symbols[symbol].type == 'output':
                    if msb == lsb: 
                        f.write(f'\t{symbol}Pin.setPinMode(3); // Output\n')
                        f.write(f'\t{symbol}Pin.setOutState(false);\n')
                    else:
                        f.write(f'\t{symbol}Port.setPinMode(3); // Output\n')
                        f.write(f'\t{symbol}Port.setOutState(0);\n')
            f.write('}\n')

            # -------------------- voltChanged function --------------------
            f.write('\nvoid voltChanged()\n{\n\t// ___implementation___\n')
            for statement in self.statements:
                f.write(f'\t{statement};\n')     
            f.write('}\n')
