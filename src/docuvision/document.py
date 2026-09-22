"""Normalized document contracts for downstream intelligence."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Document:
    document_id: str
    text: str
    mime_type: str
    language: str | None = None

def validate(document: Document) -> None:
    if not document.document_id.strip() or not document.mime_type.strip():
        raise ValueError("document_id and mime_type are required")
