from dataclasses import dataclass
import re
@dataclass(frozen=True)
class Document: id:str; text:str
@dataclass(frozen=True)
class CleanDocument: id:str; text:str; word_count:int
def normalize(doc):
 text=re.sub(r'\\s+',' ',doc.text).strip()
 return CleanDocument(doc.id,text,len(text.split()) if text else 0)
