from dataclasses import dataclass

@dataclass(frozen=True)
class QualityReport:
    word_count: int
    characters: int
    empty: bool

def assess(text: str) -> QualityReport:
    normalized = " ".join(text.split())
    return QualityReport(len(normalized.split()), len(normalized), not bool(normalized))
