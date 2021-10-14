def slugify(text: str) -> str:
    replaces = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'ñ': 'n',
        'ü': 'u',
        ' ': '-'
    }
    result = text.lower()
    for key in replaces:
        result = result.replace(key, replaces[key])
    return result
