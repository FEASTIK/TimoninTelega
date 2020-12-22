from googletrans import Translator
import googletrans


def translateText(input_text,user_name):

  translator = Translator()
  r=input_text#hi
  #result=''
  try:

    if r.find('/start')!=-1:
     return "Привет, {}. \n\nВведи /help для объяснения работы.".format(user_name)

    elif r.find('/help')!=-1:
     return "\nКак я перевожу?\n\n>  Входной язык любой. \n> Пример:\n \t  en: Я еще учусь.\n\n Чтобы увидеть список языков введите /lang.\n"

    elif r.find('/lang')!=-1:
     return googletrans.LANGUAGES

    elif r.find(':')==-1:
     result = translator.translate(input_text,dest='bn')

    elif r[2]==':': 
     s=r[3:]
     lan=r[0:2]
     result = translator.translate(s, dest=lan)  
       
    elif r[3]==':':
     s=r[4:]
     lan=r[0:2]
     result = translator.translate(s,dest=lan)
     #googletrans.LANGUAGES
     
    return result.text  

  except:
    return "Не удалось перевести. \nПопробуйте команду /help."  
    


