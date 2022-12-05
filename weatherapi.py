import requests
from bs4 import BeautifulSoup as bs

# a function to get weather information and returns a paragraph (string) full of info
def getweather() -> str:
    url = 'https://rss.weather.gov.hk/rss/SeveralDaysWeatherForecast.xml'
    try:
        r = requests.get(url)

        soup = bs(r.content, 'xml') # If this line causes an error, run 'pip install html5lib' or install html5lib
        soup.prettify()

    # on exception return the historical data
    except Exception as e:
        with open('history_weather.txt', 'r') as data:
            msg = 'something went wrong with \nweather fetching :(\nHeres the historical data instead:\n ' + str(e) + '\n\n' + data.read()

        return msg

    table = soup.find_all('description')[1]

    replaced = table.get_text()

    removetext = ['<br/>', '<p/>', '        ']

    replaced = replaced.replace('-  \n       ', '-')

    for text in removetext:
        replaced = replaced.replace(text, '')


    replaced = replaced.replace(':\n', ': ')
    replaced = replaced.replace(':       \n', ': ')
    replaced = replaced.replace('per Cent', '%\n')
    replaced = replaced.replace('.\nDate', '.\n\nDate')
    return replaced
    # when it works save a copy of the data as "history_weather_data.txt", on exception send that instead
    with open('history_weather.txt', 'w') as data:
        data.write(replaced)


