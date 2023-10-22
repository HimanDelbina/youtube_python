import speech_recognition as sr


import speech_recognition as sr

recognizer = sr.Recognizer()

audio_file = "story.mp3"

with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data, language="en-EN")
        # text = recognizer.recognize_google(audio_data, language="fa-IR")
        print("متن تشخیص داده شده: " + text)
    except sr.UnknownValueError:
        print("گفتار تشخیص داده نشد.")
    except sr.RequestError as e:
        print("خطا در درخواست به موتور تبدیل گفتار به متن: {0}".format(e))