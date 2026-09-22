from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol
@dataclass(frozen=True, slots=True)
class DocumentPage: number: int; text: str
class OCRBackend(Protocol):
    def extract(self, image: bytes) -> str: ...
class DocumentPipeline:
    def __init__(self, ocr: OCRBackend): self.ocr = ocr
    def process(self, pages: list[tuple[int, bytes]]) -> list[DocumentPage]:
        if not pages: raise ValueError("at least one page is required")
        if any(number < 1 for number, _ in pages): raise ValueError("page numbers must be positive")
        return [DocumentPage(number, self.ocr.extract(data).strip()) for number, data in pages]
