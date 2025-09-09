# Placeholder / stub for resume parsing (future work)
# Idea: use spaCy or similar for named entities, skills extraction

def extract_keywords(resume_text: str):
    """
    Very naive keyword extractor: split tokens, filter short tokens,
    remove punctuation; return unique alphabetical tokens.
    Replace with spaCy / regex / ML-based extraction later.
    """
    tokens = [t.strip(",.()[]{}:;\"'").lower() for t in resume_text.split() if len(t) > 3]
    uniq = sorted(set(tokens))
    return [t for t in uniq if t.isalpha()]