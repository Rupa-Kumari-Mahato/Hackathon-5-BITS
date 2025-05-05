from gtts import gTTS
import pygame
import time
import os

def speak_text(text, lang='en'):
    filename = "output.mp3"
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Wait until audio finishes 
    while pygame.mixer.music.get_busy():
        time.sleep(0.5)

    pygame.mixer.quit()
    os.remove(filename)  # Clean-up

# Example usage
speak_text("स्वागत है! आज हम वायुमंडल के बारे में पढ़ेंगे।", lang='hi')  # Hindi
speak_text("Welcome to the adaptive learning platform.", lang='en')     # English
speak_text("আমি আমার মা বাবা এবং দিদি এবং সেরা বন্ধুকে ভালবাসি.", lang='bn')     # Bengali
speak_text("पढ़ाई एगो लइका खातिर सबसे बढ़िया आशीर्वाद होला.", lang='bn')     # Bhojpuri
speak_text("मै पहाड़, प्रकृति अउर ओकर शांति से प्रेम करै छी.", lang='bn')     #Khotta 