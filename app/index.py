DOCS = {}


def add(doc_id, text):
    DOCS[doc_id] = text.lower().split()


def search(term):
    return sorted(d for d, words in DOCS.items() if term.lower() in words)


ROUTES = {"/index/size": lambda: {"docs": len(DOCS)}}
