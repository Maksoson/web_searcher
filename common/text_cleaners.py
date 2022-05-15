import re


def remove_header_tags_with_content(text):
    return re.sub(r'<header\b[^<]*(?:(?!<\/header>)<[^<]*)*<\/header>', '', text)


def remove_footer_tags_with_content(text):
    return re.sub(r'<footer\b[^<]*(?:(?!<\/footer>)<[^<]*)*<\/footer>', '', text)


def remove_script_tags_with_content(text):
    return re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', text)


def remove_image_tags_with_content(text):
    return re.sub(r'<img\b[^<]*(?:(?!<\/img>)<[^<]*)*<\/img>', '', text)


def remove_all_tags(text):
    return re.sub(r'(<([^>]+)>)', ' ', text)


def remove_specials(text):
    return re.sub(r'(\\n)|(\\r)|( - )|( — )', ' ', text)


def remove_symbols(text):
    return re.sub(r'[\[\\\^$\.\|\?\*+\(\)\]\/,!:↑↓&%;\'"_=“«»#●→©{}<>]', ' ', text)


def remove_duplicate_spaces(text):
    return ' '.join(text.split())


def clean(text):
    text = remove_header_tags_with_content(text)
    text = remove_footer_tags_with_content(text)

    text = remove_script_tags_with_content(text)
    text = remove_image_tags_with_content(text)

    text = remove_all_tags(text)
    text = remove_specials(text)
    text = remove_symbols(text)
    text = remove_duplicate_spaces(text)

    return text
