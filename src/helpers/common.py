from flask import request
import glob
import json

def getLocales(names: list):
        locale = request.cookies.get('locale', 'en')
        languages = {}
        localeFile = "languages/"+locale+"/*.json"
        filePathEn = glob.glob(localeFile)
        for lang in filePathEn:
            filename = lang.split('\\')
            keyName = filename[1].split('.')[0]
            with open(lang, 'r', encoding='utf8') as file:
                languages[keyName] = json.loads(file.read())
        
        response = {}
        for name in names:
            if name in languages:
                response[name] = languages[name]
            
        response.update({'currentLocale': locale})
        return response