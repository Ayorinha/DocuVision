from dataclasses import dataclass
from typing import Protocol
@dataclass(frozen=True)
class DocumentPage:number:int;text:str
class OCRBackend(Protocol):
 def extract(self,image:bytes)->str:...
class DocumentPipeline:
 def __init__(self,ocr):self.ocr=ocr
 def process(self,pages):
  if any(n<1 for n,_ in pages):raise ValueError("page numbers must be positive")
  return [DocumentPage(n,self.ocr.extract(data).strip()) for n,data in pages]
