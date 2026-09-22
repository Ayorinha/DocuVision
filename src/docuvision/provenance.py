"""Document provenance primitives."""
from hashlib import sha256
def content_fingerprint(text: str) -> str:
    if not isinstance(text,str): raise TypeError("text must be a string")
    return sha256(text.encode("utf-8")).hexdigest()