from grab import Grab
import re

number = 0
cYears = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
cCountry = ['США', 'Россия', 'Япония', 'Китай', 'Испания']
сQuality = ['HDRip', 'WEBRip']
cLanguage = ['Профессиональный', 'Дублированный']
cLinkFilms = [
 "http://kinogo.club/biografii/",
 "http://kinogo.club/boeviki/",
 "http://kinogo.club/vesterny/",
 "http://kinogo.club/voennye/",
 "http://kinogo.club/detektivy/",
 "http://kinogo.club/detskie/",
 "http://kinogo.club/dokumentalnye/",
 "http://kinogo.club/dramy/",
 "http://kinogo.club/istoricheskie/",
 "http://kinogo.club/komedii/",
 "http://kinogo.club/kriminal/",
 "http://kinogo.club/melodramy/",
 "http://kinogo.club/multfilmy/",
 "http://kinogo.club/mjuzikly/",
 "http://kinogo.club/otechestvenie/",
 "http://kinogo.club/prikljuchenija/",
 "http://kinogo.club/semejnye/",
 "http://kinogo.club/sportivnye/",
 "http://kinogo.club/trillery/",
 "http://kinogo.club/uzhasy/",
 "http://kinogo.club/fantastika/",
 "http://kinogo.club/fjentjezi/",
 "http://kinogo.club/amerikanskye_filmy/",
 "http://kinogo.club/anglijskie_filmy/",
 "http://kinogo.club/russkie_filmy/",
 "http://kinogo.club/indiyskie_filmy/",
 "http://kinogo.club/nemeckie_filmy/",
 "http://kinogo.club/francuzskie_filmy/",
 "http://kinogo.club/russkye_serialy/",
 "http://kinogo.club/zarubezhnye_serialy/",
 "http://kinogo.club/turezkie_serialy/"
]

cLinkFilmsRus = [
 "Биографии",
 "Боевики",
 "Вестерны",
 "Военные",
 "Детективы",
 "Детские",
 "Документальные",
 "Драмы",
 "Исторические",
 "Комедии",
 "Криминал",
 "Мелодрамы",
 "Мультфильмы",
 "Мюзиклы",
 "Отечественные",
 "Приключения",
 "Семейные",
 "Спортивные",
 "Триллеры",
 "Ужасы",
 "Фантастика",
 "Фэнтези",
 "Американские фильмы",
 "Английские фильмы",
 "Русские фильмы",
 "Индийские фильмы",
 "Немецкие фильмы",
 "Французские фильмы",
 "Русские сериалы",
 "Зарубежные сериалы",
 "Турецкие сериалы"
]

mNamesOfFilms = []  # массив для имен фильмов
mDateOfFilmsCreats = []  # массив для даты создания фильмов
mCountryOfFilmsCreats = []  # массив для стран в которых создали фильмы
mQualityOfFilms = []  # массив для качества фильмов
mLanguageOfFilms = []  # массив для перевода
mTimeOfFilms = []  # массив для продолжительности фильмов
mDescription = []  # массив для описания фильмов
mRatings = []  # массив для рейтинга
mNumberOfPages = []  # для количества страниц

g = Grab(log_file='out.html')

file = open('parsing.xml', 'a')
file.write('<?xml version="1.0" encoding="windows-1251" standalone="yes"?>' + '\n')
file.write('<data-set xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">' + '\n')

"""
Функция для запуска функций получения
имен, качества, перевода, года, страны,
продолжительности, описания фильмов
"""


def all_films(link):
    for counter in range(0, 10):
        file.write('<record>' + '\n')
        file.write('<FilmName>' + str(names_of_films('//h2[@class="zagolovki"]', link)[counter]) + '</FilmName>')
        file.write('<Quality>' + str(quality_of_films('//div[@class = "shortimg"]', link)[counter]) + '</Quality>')
        file.write('<Rating>' + str(film_ratings('//li[@class = "current-rating"]', link)[counter]) + '</Rating>')
        file.write('<Translate>' + str(language_of_films('//div[@class = "shortimg"]', link)[counter]) + '</Translate>')
        file.write('<Year>' + str(date_of_films_creation('//div[@class = "shortimg"]', link)[counter]) + '</Year>')
        file.write('<Country>' + str(country_of_films('//div[@class = "shortimg"]', link)[counter]) + '</Country>')
        file.write('<Duration>' + str(time_of_films('//div[@class = "shortimg"]', link)[counter]) + '</Duration>')
        file.write('<About>' + str(short_description('//div[@class = "shortimg"]', link)[counter]) + '</About>')
        file.write('</record>' + '\n')
    return print("Спарсена информация с ссылки : " + link)


"""
Функция получения имен фильмов
"""


def names_of_films(link, site):  # имена фильмов
    g.go(site)
    for NameOfFilm in g.xpath_list(link):
        mNamesOfFilms.append(NameOfFilm.text_content())
    return mNamesOfFilms

"""
Функция получения даты создания фильмов
"""


def date_of_films_creation(link, site):
    g.go(site)
    for AboutFilm in g.xpath_list(link):
        flag = False
        for WordsInAboutFilm in (AboutFilm.text_content()).split(" "):
            for year in cYears:
                if str(year) in WordsInAboutFilm:
                    mDateOfFilmsCreats.append(year)
                    flag = True
            if flag is True:
                break
        if flag is False:
            mDateOfFilmsCreats.append("null")
    return mDateOfFilmsCreats

"""
функция получения страны создания фильма
"""


def country_of_films(link, site):
    g.go(site)
    for AboutFilm in g.xpath_list(link):
        flag = False
        for WordsInAboutFilm in (AboutFilm.text_content()).split(" "):
            for country in cCountry:
                if str(country) in WordsInAboutFilm:
                    mCountryOfFilmsCreats.append(country)
                    flag = True
            if flag is True:
                break
        if flag is False:
            mCountryOfFilmsCreats.append("null")
    return mCountryOfFilmsCreats

"""
функция получения рейтинга
"""


def film_ratings(link, site):
    g.go(site)
    for i in g.xpath_list(link):
        mRatings .append(i.text_content())
    return mRatings

"""
Функция получения качества фильмов
"""


def quality_of_films(link, site):
    g.go(site)
    for AboutFilm in g.xpath_list(link):
        flag = False
        for WordsInAboutFilm in (AboutFilm.text_content()).split(" "):
            for quality in сQuality:
                if str(quality) in WordsInAboutFilm:
                    mQualityOfFilms.append(quality)
                    flag = True
            if flag is True:
                break
        if flag is False:
            mQualityOfFilms.append("null")
    return mQualityOfFilms

"""
Функция получения перевода фильмов
"""


def language_of_films(link, site):
    g.go(site)
    for AboutFilm in g.xpath_list(link):
        flag = False
        for WordsInAboutFilm in (AboutFilm.text_content()).split(" "):
            for language in cLanguage:
                if str(language) in WordsInAboutFilm:
                    mLanguageOfFilms.append(language)
                    flag = True
            if flag is True:
                break
        if flag is False:
            mLanguageOfFilms.append("null")
    return mLanguageOfFilms

"""
Функция получения продолжительности фильмов
"""


def time_of_films(link, site):
    g.go(site)
    for AboutFilm in g.xpath_list(link):
        for WordsInAboutFilm in (AboutFilm.text_content()).split(" "):
            m = re.search('\d\d:\d\d:\d\d', WordsInAboutFilm)
            if m:
                mTimeOfFilms.append(m.group())
    return mTimeOfFilms

"""
Функция получения описания фильмов
"""


def short_description(link, site):
    g.go(site)
    for AboutFilm in g.xpath_list(link):
        FirstNumberOfWords = 0
        description = 0
        for words in AboutFilm.text_content().split(" "):
            description = description + len(words)
            FirstNumberOfWords = FirstNumberOfWords + 1
            if words == "" or words == " ":
                description += 1
            if "..." in words:
                mDescription.append(AboutFilm.text_content()[0:description + FirstNumberOfWords - 4])
    return mDescription


"""
Функция старта парсинга по параметрам которые передает пользователь
"""


"""
функция получения количества страниц для каждого типа фильмов,
в ней баг если количество страниц меньше 10 функция не может найти
количество
"""


def number_of_pages():
    for link in cLinkFilms:
        g.go(link)
        for numbersoflinks in g.xpath_list('//div[@class = "bot-navigation"]'):
            tempmassiv = numbersoflinks.text_content().split(" ")
        mNumberOfPages.append(tempmassiv[len(tempmassiv) - 2])
    counter = -1
    for count in mNumberOfPages:
        counter += 1
        if count == "":
            mNumberOfPages[counter] = "Не удалось определить количество "
    return mNumberOfPages


def start_parsing(typeoffilm, numberofpage):
    for i in range(1, int(numberofpage) + 1):
        all_films(cLinkFilms[int(typeoffilm)] + 'page/' + str(i) + "/")
    file.write('</data-set>' + '\n')
    file.close()


def ask_user_what_parse():
    print("Подождите секунд 10 ... Сканируем количество страниц")
    number_of_pages()
    typeoffilmflag = False
    for i in range(0, 31):
        print(str(i) + ". " + cLinkFilmsRus[i] + " " + mNumberOfPages[i] + " страниц")
    print("Введи номер какие фильмы нужно парсить: ")
    typeoffilm = input()
    try:
        typeoffilm = int(typeoffilm)
        if typeoffilm not in range(0, 31):
            print("Введено число которое не в диапазоне")
        else:
            typeoffilmflag = True

    except ValueError:
        print("Это не целое число, парсер закрывается")

    if typeoffilmflag is True:
        print("Введи количество страниц которое нужно спарсить: ")
        numberofpage = input()
        try:
            numberofpage = int(numberofpage)

            if int(numberofpage) not in range(0, int(mNumberOfPages[typeoffilm])):
                print("Программа может завершится по причине того что введено число которое не входит в диапазон")
            start_parsing(typeoffilm, numberofpage)

        except ValueError:
            print("Это не целое число, парсер закрывается")


ask_user_what_parse()
