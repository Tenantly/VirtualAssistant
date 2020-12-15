import requests
import xml.etree.cElementTree as ET

name_value = input("Название валюты USD или EUR: ")
value = int(input("Количество конвертируемых рублей: "))

get_xml = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
structure = ET.fromstring(get_xml.content)

if name_value == "USD":
    dollar = structure.find("./*[@ID='R01235']/Value")
    result = float(dollar.text.replace(',', '.'))
    print(value/result, "Долларов")

if name_value == "EUR":
    dollar = structure.find("./*[@ID='R01239']/Value")
    result = float(dollar.text.replace(',', '.'))
    print(value/result, "Евро")
