"""Production smoke tests for DocuVision."""
import importlib

def test_package_imports() -> None:
    module = importlib.import_module("docuvision")
    assert module.__name__ == "docuvision"
