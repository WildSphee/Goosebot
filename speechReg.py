# import speech_recognition as sr
# import constant as keys


def inputSpeech():
    r = sr.Recognizer()

    with sr.WavFile("newvoice.wav") as source:  # use "test.wav" as the audio source
        user_audio = r.record(source)  # extract audio data from the file

    text = r.recognize_google(user_audio, language='en-US')

    print(text)
    return text




# inputSpeech()
