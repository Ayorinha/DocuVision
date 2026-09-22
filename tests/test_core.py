from docuvision.core import *

class Fake:\n def extract(self,image):return " text "\ndef test_pipeline():assert DocumentPipeline(Fake()).process([(1,b"x")])[0].text=="text"
