from docuvision.quality import assess

def test_assess_document_quality():
    report=assess("  contrato   digital ")
    assert report.word_count==2
    assert report.characters==16
    assert report.empty is False
