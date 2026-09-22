from docuvision.pipeline import *
def test_normalize(): assert normalize(Document('1',' a\\n b ')).word_count==2
