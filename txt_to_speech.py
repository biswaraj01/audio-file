from gtts import gTTS

language = 'en'
text = 'Hello World!'

speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
speech.save('voice.mp3')
