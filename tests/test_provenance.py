from docuvision.provenance import content_fingerprint
def test_fingerprint_is_stable(): assert content_fingerprint("abc")==content_fingerprint("abc")