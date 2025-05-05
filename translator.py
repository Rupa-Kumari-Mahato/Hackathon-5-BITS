# utils/translate.py

from googletrans import Translator as GoogleTranslator
from googletrans.constants import LANGUAGES


class Translator:
    def __init__(self, src_lang='auto', target_lang='hi'):
        """
        Initialize the Translator with source and target language codes.
        :param src_lang: Language code to detect from (default is 'auto')
        :param target_lang: Target language code (e.g., 'hi' for Hindi)
        """
        self.src_lang = src_lang
        self.target_lang = target_lang
        self.translator = GoogleTranslator()

    def translate(self, text):
        """
        Translate the given text to the target language.
        :param text: str
        :return: str (translated text)
        """
        try:
            if not text:
                return ""

            translated = self.translator.translate(
                text, src=self.src_lang, dest=self.target_lang
            )
            return translated.text

        except Exception as e:
            print(f"[Translation Error] {e}")
            return text  # Return original text if translation fails

    @staticmethod
    def get_supported_languages():
        """
        Returns supported language codes and their names.
        :return: dict
        """
        return LANGUAGES
