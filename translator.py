from typing import Literal

# Toy bilingual/trilingual dictionary for demo purposes.
# In production, swap with a real translation engine or model.
DICTIONARY = {
    # English -> Hindi (hi) & Telugu (te)
    ("en", "hi"): {
        "hello": "नमस्ते",
        "job": "नौकरी",
        "resume": "बायोडाटा",
        "software engineer": "सॉफ़्टवेयर इंजीनियर",
        "data analyst": "डेटा विश्लेषक"
    },
    ("en", "te"): {
        "hello": "నమస్తే",
        "job": "ఉద్యోగం",
        "resume": "ప్రత్యేక చరిత్ర",
        "software engineer": "సాఫ్ట్‌వేర్ ఇంజనీర్",
        "data analyst": "డేటా విశ్లేషకుడు"
    },
    # Hindi -> English
    ("hi", "en"): {
        "नमस्ते": "hello",
        "नौकरी": "job",
        "बायोडाटा": "resume",
        "सॉफ़्टवेयर इंजीनियर": "software engineer",
        "डेटा विश्लेषक": "data analyst"
    },
    # Telugu -> English
    ("te", "en"): {
        "నమస్తే": "hello",
        "ఉద్యోగం": "job",
        "ప్రత్యేక చరిత్ర": "resume",
        "సాఫ్ట్‌వేర్ ఇంజనీర్": "software engineer",
        "డేటా విశ్లేషకుడు": "data analyst"
    },
}

SupportedLang = Literal["en", "hi", "te"]

def translate(text: str, src: SupportedLang, tgt: SupportedLang) -> str:
    """
    Naive word-by-word translator using DICTIONARY mapping.
    Meant as a demo stub: replace with a proper MT model / API for production.
    """
    if src == tgt:
        return text
    key = (src, tgt)
    mapping = DICTIONARY.get(key, {})
    # token-by-token mapping; preserves unknown tokens as-is
    out = []
    for token in text.lower().split():
        out.append(mapping.get(token, token))
    return " ".join(out)