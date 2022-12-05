import weatherapi
from futustocks.mailsender import sendMail
from time import localtime


# everyday this script would be triggered, and send an email with info of the weather
def main():
    lt = localtime()
    subject = f'{lt.tm_year}-{lt.tm_mon}-{lt.tm_mday} Weather Report :)'

    body = weatherapi.getweather() + '\n\nHave a nice day ahead :)\nGooseBot'

    # print(f'{subject=} \n {body=}')

    sendMail(subject=subject, body=body)


if __name__ == '__main__':
    main()
