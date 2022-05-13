import requests as r
from deep_translator import GoogleTranslator
from random import randint

translator = GoogleTranslator(source='en', target='fa')
tozih=translator.translate("I use an API for translation so it might not be correct all the time.")

class Crypocurrencies:
        def crypto(url):
            res=r.get(url)
            s=res.json()['data']
            info=''
            num=1
            for i in s:
                if i['rank'] == num:
                    info+=f"{i['rank']} - {i['name']} {i['price_usd']}$ \n"
                    num+=1
            extraC=sorted([55353,42859])
            for i in extraC:
                res=r.get("https://api.coinlore.net/api/ticker/?id=%i" % i).json()[0]
                info+=f"{res['rank']} - {res['name']} {res['price_usd']}$ \n"
            return info

class Excuse:
    def excuse_maker(url):
        res= r.get(url)
        category = res.json()[0]['category']
        excuse = res.json()[0]['excuse']
        cat = translator.translate(f"category : {category}")
        exc = translator.translate(excuse)
        exc_text = excuse + '\n\n' + category + '\n\n\n' + exc + '\n\n' + cat 
        return exc_text

class Quotes:
    def quote(url):
        get=r.get(url)
        text = get.json()['data']['quote']
        author = get.json()['data']['author']
        translation = translator.translate(text)
        text = text.strip('@#')
        msg = text + '\n \n' + f'"{author}"' + '\n \n' + translation  #+ '\n \n'  + ptext 
        return msg

class Meme:
    def meme(url):
        random=randint(1,100)
        res=r.get(url).json()['data']['memes'][random]['url']
        return res

class UselessFacts:
        def useless_facts(url):
            res=r.get(url).json()['text']
            fa_res=translator.translate(res)
            res=res + '\n\n' + fa_res
            return res

if __name__ == '__main__':
    exit()