import pytest


@pytest.mark.order(1)
class TestImport(object):
    def test_import(self):
        import fedtoy
