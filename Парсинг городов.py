import requests
from bs4 import BeautifulSoup
from lxml import html

#Блок в котором мы заходим на сайт с уже выбранной областью
link = 'https://world-weather.ru/pogoda/russia/vologda_oblast/' #сюда можно вставить ссылку на любую область с данного сайта
resource = requests.get(link).text
soup = BeautifulSoup(resource, "lxml")
goroda = soup.find_all('li', class_ = 'city-block')

#Блок который парсит список городов и сохраняет их
#в файл GORODA.txt (в списке 2 города БАБАЕВО это ошибка на сайте)
mass = []
for i in goroda:
   name = i.find('a').text
   mass.append(name)
   with open('GORODA.txt', 'w', encoding='utf=8') as file:
       for u in mass:
           file.write(u + '\n')

#Блок который выводит содержимое
#файла GORODA.txt
with open ("GORODA.txt", "r") as f:
   GORODA = f.read()
   print(GORODA)

# Создаем переменную в которую записываем город,
# в котором хотим узнать температуру
imya_goroda = input('Введите название города: ')

#Перебираем файл с городами и сравниваем
# введенный нами город со списком городов
file1 = open ('GORODA.txt', 'r')
lines = file1.readlines()
for line in lines:
    if line.strip() == imya_goroda:
        #print(imya_goroda)
        response1 = requests.get(link) #('https://world-weather.ru/pogoda/russia/vologda_oblast/')
        parsed_body = html.fromstring(response1.text)
        a = parsed_body.xpath('//a[text()="%s"]/@href'%line.strip())#парсим ссылку для выбранного города,ссылка без https:, на данный момент ссылка не рабочая
        b = 'https:' + a[0]#соединяем ссылку и https чтобы ссылка стала рабочей
        resource2 = requests.get(b).text
        soup = BeautifulSoup(resource2, "lxml")
        gorod = soup.find('h1')
        den_nedeli = soup.find_all('div', class_='day-week')
        temperatura = soup.find_all('div', class_='day-temperature')
        for item in gorod:
            print(item.text)
            for item1 in range(len(den_nedeli)):
                print(den_nedeli[item1].text)
                for item2 in range(len(temperatura)):
                    if item1 == item2:
                        print(temperatura[item2].text)
    # else:
    #     print('Такого города нет ! ! !')
    #     break #Для того чтобы прекратить работу цикла


    #! ! ! Если раскоментить блок else то через определенное
    # количество запусков скрипта, скрипт перестает
    # правильно работать, подозреваю что в этом виноват
    # каким то образом сам сайт ! ! ! !







