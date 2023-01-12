from classFiles import JSONFileMethod, XMLFileMethod,FlatFileMethod

# Realiza los calculos del archivo flat
flat_ = FlatFileMethod()
flat_.template_method()

with open('Archivos/file.flat.out') as file:
    archivo = file.read()
    print(f"Datos del archivo flat: \n {archivo}")
    print("----------------------------------------------------------------")
    
# Realiza los calculos del archivo json
Json_ = JSONFileMethod()
Json_.template_method()

with open('Archivos/file.json.out', 'r') as file:
    archivo = file.read()
    print(f"Datos del archivo JSON: \n {archivo}")
    print("----------------------------------------------------------------")
    print("\n") 

# Realiza los calculos del archivo XML
xml_ = XMLFileMethod()
xml_.template_method()

with open('Archivos/file.xml.out', 'r') as file:
    archivo = file.read()
    print(f"Datos del archivo XML file: \n {archivo}")
    print("----------------------------------------------------------------")
    print("\n") 


