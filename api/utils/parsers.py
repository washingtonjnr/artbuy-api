import re
import phonenumbers


def remove_nom_numeric_chars(s: str, exceptions=[]) -> str:
    if not s:
        return s
    regexp = "[^0-9{}]".format("".join(exceptions))

    return re.sub(regexp, "", s)


def normalize_email(s: str) -> str:
    if s:
        s = re.sub(r"\s+", "", s).lower()

    return s


def format_phonenumber(number: str):
    try:
        parsed = phonenumbers.parse(number)
        return f"+{parsed.country_code}-{parsed.national_number}"
    except Exception:
        return remove_nom_numeric_chars(number, ["+"])
