import re

def parse_json_to_xml(json_string):
    xml_string = ""
    json_dict = eval(json_string)  # Преобразуем JSON-строку в Python словарь через eval()

    for key, value in json_dict.items():
        key = re.sub(r'\s+', '', key)  # Убираем пробелы из имени тега

        xml_string += f"<{key}>"

        if isinstance(value, dict):  # Если значение является словарем
            xml_string += parse_dict_to_xml(value)
        elif isinstance(value, list):  # Если значение является списком
            xml_string += parse_list_to_xml(value)
        else:
            value = re.sub(r'\s+', '', str(value))  # Убираем пробелы из значения
            xml_string += value

        xml_string += f"</{key}>"

    return xml_string

def parse_dict_to_xml(json_dict):
    xml_string = ""
  
    for key, value in json_dict.items():
        key = re.sub(r'\s+', '', key)  # Убираем пробелы из имени тега

        xml_string += f"<{key}>"

        if isinstance(value, dict):
            xml_string += parse_dict_to_xml(value)
        elif isinstance(value, list):
            xml_string += parse_list_to_xml(value)
        else:
            value = re.sub(r'\s+', '', str(value))  # Убираем пробелы из значения
            xml_string += value

        xml_string += f"</{key}>"

    return xml_string

def parse_list_to_xml(json_list):
    xml_string = ""
  
    for item in json_list:
        if isinstance(item, dict):
            xml_string += parse_dict_to_xml(item)
        elif isinstance(item, list):
            xml_string += parse_list_to_xml(item)
        else:
            item = re.sub(r'\s+', '', str(item))  # Убираем пробелы из значения
            xml_string += item

    return xml_string

# Пример использования
json_string = '{"name": "John", "age": 30, "hobbies": ["football", "drawing"], "address": {"street": "123 Main St", "city": "New York"}}'
xml_string = parse_json_to_xml(json_string)

# Убираем пробелы и круглые скобки из тегов XML
xml_string = re.sub(r'\s+<', '<', xml_string)
xml_string = re.sub(r'>\s+', '>', xml_string)

print(xml_string)
