# Libraries, packages etc
# import nltk
# nltk.download()
from nltk.stem import SnowballStemmer
from langdetect import detect
# Django
from django.db.models.signals import post_save
from django.dispatch import receiver
# Django apps
from .models import *
from common.constants.lang import STEMMER_LANGUAGES


@receiver(post_save, sender=PageContent)
def page_content_save_action(sender, instance: PageContent, created: PageContent, **kwargs):
    # Split text and stemming words (losses if text language contains words from other languages)
    def stem_and_count_words(text):
        if text is not None:
            for raw_word in text.split(' '):
                stemmed_word = stemmer.stem(raw_word)

                if stemmed_word.strip() == '':
                    continue

                if words_count.get(stemmed_word):
                    words_count[stemmed_word] += 1
                else:
                    words_count.setdefault(stemmed_word, 1)

    # { 'stemmed_word': count_in_text }
    # { string: integer }
    words_count = {}

    # Detecting text language
    lang_code = detect(instance.content)
    if lang_code is None:
        lang_code = 'po'
    stemmer = SnowballStemmer(STEMMER_LANGUAGES[lang_code], True)

    stem_and_count_words(instance.content)
    stem_and_count_words(instance.meta_title)
    stem_and_count_words(instance.meta_description)
    stem_and_count_words(instance.meta_keywords)

    for word in words_count.keys():
        Word.objects.update_or_create(
            value=word,
            page=instance,
            defaults={
                'value': word,
                'page': instance,
                'count': words_count[word]
            })
