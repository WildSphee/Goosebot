import random
from random import choice

# 'weather'
import weatherapi

# 'mail weather'
import mail_me_everyday

# 'quote "something"'
from futustocks import futumain


honks1 = ["HONK!", "honk~", "honk honk?", "Honk...", "Honk Honk :)"]

honks2 = ["Honk honk honk... HONK!", "HONK HONK HONK!!", "HoNk??????", "honk honk, honk honk honk!"]

honks3 = ["HONKHOONKHONKKKKK!!!!!", "HOKNHOKHNOHKNHOKHNHOKHNHOK", "HOnk honk honk? HONK HONK!!!",
          "honk, honk! honk honk honk honk honk? honkhonkhonk!!! honk, honkhonk - honk. honk, honk honkhonk~"]


def reply(inputtext) -> str:

    # it stands for input text haha
    # pit is pre-lowered text
    pit = inputtext.split()
    it = [x.lower() for x in pit]

    # if they want to ask for a quote on a stock code
    if it[0] == 'quote':
        result = None

        if len(it) == 1:
            result = futumain.getquote()
        elif len(it) == 2:
            result = futumain.getquote(target=it[1].upper())
        elif len(it) >= 3:
            result = futumain.getquote(target=it[1].upper(), starttime=futumain.showtime(int(it[2])))
        else:
            print('unknown error')

        if result:
            return result
        else:
            return 'Failed to get from Futu API'


    # if ask to get weather as mail
    if len(it) == 2 and it[0] == 'mail' and it[1] == 'weather':
        mail_me_everyday.main()
        return 'Mail Sent'

    # if asking for weather (weather)
    if len(it) == 1 and it[0] == "weather":
        return weatherapi.getweather()

    # test if its a probability (eg 1 in 3)
    if len(it) == 3 and it[1] == 'in':
        try:
            son, _, mom = it
            chance = (float(son)/float(mom)) *100
            r = f'{son} in {mom} = {chance:.2f}% {chr(10)}'

            rannum = random.random()
            if rannum <= chance/100:
                r += f'HIT at {rannum:.3f}'
            else:
                r += f'MISS at {rannum:.3f}'

            return r

        except Exception:
            print('an exception in fraction prob')
            pass

    text = str(inputtext).lower()
    # r = responses.sample_response(text)
    length = len(text.split())
    if length <= 2:
        r = choice(honks1)
    elif length <= 4:
        r = choice(honks2)
    else:
        r = choice(honks3)

    return r