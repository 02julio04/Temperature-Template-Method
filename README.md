# Template Method 

### Temperature Data : Minimo, Maximo, Average
-----------------
-----------------
### Archivos:
- Flat File
```html
id|location|date|measure
1|Pensilvania|2020-01-12|25.6
2|Brooklyn|2020-01-12|21.2
3|Boston|2020-01-12|36.4
 ```
- JSON
```html
{
    "location": "Pensilvania",
    "measures": [
      {"date": "2020-01-12", "temperature": 15.5},
      {"date": "2020-01-12", "temperature": 22.2},
      {"date": "2020-01-12", "temperature": 27.3}
    ]
  }
  ```
- XML File

```html
<?xml version="1.0" encoding="UTF-8"?>
<data>
    <row>
        <id>1</id>
        <location>Santo Domingo</location>
        <date>2020-01-12</date>
        <measure>21.3</measure>
    </row>
    <row>
        <id>2</id>
        <location>Atlante</location>
        <date>2020-01-12</date>
        <measure>29.1</measure>
    </row>
     <row>
        <id>3</id>
        <location>Panama</location>
        <date>2020-01-12</date>
        <measure>19.3</measure>
    </row>
</data>
```

# Diagrama UML

[![Diagrama-en-blanco-P-gina-3.png](https://i.postimg.cc/FKWnq8Hv/Diagrama-en-blanco-P-gina-3.png)](https://postimg.cc/PLD4v6DV)

