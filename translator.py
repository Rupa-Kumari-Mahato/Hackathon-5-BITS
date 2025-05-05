from googletrans import Translator

print("Simple Language Translator")
text = input("Enter text to translate: ")
print(f"You entered: {text}")

src_language = input("Enter source language code (e.g., 'en' for English): ")
dest_language = input("Enter destination language code (e.g., 'fr' for French): ")

translator = Translator()
try:
    translated_text = translator.translate(text, src=src_language, dest=dest_language).text
    print(f"Translated Text: {translated_text}")
except Exception as e:
    print(f"Translation failed: {e}")