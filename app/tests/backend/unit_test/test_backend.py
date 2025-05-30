import pytest
from app.src.backend.main import hello_world


#@pytest.mark.unit_test
class TestBackEnd:

    def test_hello_word(self):
        """This is a test to validate main works as expected"""
        
        expected = 'hello world'
        actual = hello_world()
        assert actual == expected

