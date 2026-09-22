from docuvision.document import Document,validate

def test_document_contract(): validate(Document("d1","hello","text/plain","en"))
