def theme_present(text, keywords):
    if not text:
        return False

    text = text.lower()
    return any(keyword in text for keyword in keywords)
