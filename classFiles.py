import json
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from abc import ABC, abstractmethod

class Tempmethod(ABC):
    def template_method(out):
          # guardo la data en los archivos out
        data = out.transform()
        tempMin, tempMax, tempAvg = out.process(data)
        out.file_data(tempMin, tempMax, tempAvg)


    @abstractmethod
    def transform(out):
        # transformo la data 
        pass

    def process(out, data):
        # Proceso la data y calculo el min, max, y el average
        temperatures = out.extract(data)
        tempMin = min(temperatures)
        tempMax = max(temperatures)
        tempAvg = sum(temperatures) / len(temperatures)
        return tempMin, tempMax, tempAvg

    @abstractmethod
    def extract(out, data):
        
        pass

    @abstractmethod
    def file_data(out, tempMin, tempMax, tempAvg):
        # paso data a los archivos correspondientes
        pass
#Clases para cada archivo
class XMLFileMethod(Tempmethod):
    def transform(out):
        tree = ET.parse('Archivos/file.xml')
        root = tree.getroot()
        return root
    
    def extract(out, data):
        temperatures = [float(row.find('measure').text) for row in data.findall('row')]
        return temperatures

    def file_data(out, min, max, avg):
        data = {'minimo': min, 'maximo': max, 'average': avg}
        root = ET.Element('temperatures')
        for key, value in data.items():
            element = ET.SubElement(root, key)
            element.text = str(value)
        tree = ET.ElementTree(root)
        xml_str = ET.tostring(root, 'utf-8')
        reparsed = minidom.parseString(xml_str)
        with open('Archivos/file.xml.out', 'w') as f:
            f.write(reparsed.toprettyxml(indent='  '))

class JSONFileMethod(Tempmethod):
    def transform(out):
        with open('Archivos/file.json') as f:
            data = json.load(f)
        return data
    
    def extract(out, data):
        temperatures = [measure['temperature'] for measure in data['measures']]
        return temperatures
    
    def file_data(out, min, max, avg):
        data = {'minimo': min, 'maximo': max, 'average': avg}
        with open('Archivos/file.json.out', 'w') as f:
            json.dump(data, f)

class FlatFileMethod(Tempmethod):
    def transform(out):
        with open('Archivos/file.flat') as f:
            data = f.readlines()
        return data
    
    def extract(out, data):
     temperatures = []
     for line in data[1:]:
        temperature = float(line.split('|')[-1])
        temperatures.append(temperature)
        return temperatures

    def file_data(out, min, max, avg):
        data = {'minimo': min, 'maximo': max, 'average': avg}
        with open('Archivos/file.flat.out', 'w') as f:
            for key, value in data.items():
                f.write(f'{key}: {value}\n')

