from flask import request
import json
import re

def translation(names: list):
        locale = request.cookies.get('locale', 'en')
        languages = {'locale': locale}
        for lang in names:
            filePath = "languages/"+locale+"/"+lang+".json"
            with open(filePath, 'r', encoding='utf8') as file:
                languages[lang] = json.loads(file.read())
            
        def t (key: str, options: dict = {}):
            listKeys = key.split('.')
            localeValue = key
            tempLocales = languages
            for localeKey in listKeys:
                if (localeKey not in tempLocales):
                    break
                else:
                    tempLocales = tempLocales[localeKey]
                    print(tempLocales, localeKey)
                    if isinstance(tempLocales, str):
                        localeValue = tempLocales
                        
            if '{' in localeValue:
                variables: list[str] = re.findall(r"\{(\w+)\}", localeValue)
                for variable in variables:
                    if variable in options:
                        localeValue = localeValue.replace("{"+variable+"}", options[variable])
            return localeValue
        
        return [languages, t]