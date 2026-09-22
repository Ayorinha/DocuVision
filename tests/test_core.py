from docuvision.core import DocumentPipeline
class OCR:
    def extract(self, image): return " extracted text "
def test_pipeline(): assert DocumentPipeline(OCR()).process([(1, b"x")])[0].text == "extracted text"
