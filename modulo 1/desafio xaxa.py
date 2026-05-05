from deep_translator import GoogleTranslator
from time import sleep
texto = "Eu te amo"

idiomas = [
"en","es","fr","de","it","ru","ja","ko","zh-CN","ar",
"hi","tr","nl","pl","sv","fi","no","da","el","he",
"th","vi","id","ms","uk","cs","ro","hu","sk","bg",
"hr","sr","sl","et","lv","lt","fa","ur","bn","ta",
"te","ml","kn","gu","mr","ne","si","my","km","lo"
]
print('Em portugues falamos um "Eu te amo"\nmas e se quisesse saber de 100 linguas?\nQue bom que fiz esse código!')
sleep(8)
for idioma in idiomas:
    try:
        traducao = GoogleTranslator(source="pt", target=idioma).translate(texto)
        print(f"{idioma}: {traducao}")
    except:
        print(f"Erro no idioma {idioma}")