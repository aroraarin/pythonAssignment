from Validation import Valid
class TestSolution:

    def test_validator(self):
        instance = Valid()
        assert instance.validator("X X X X X")==True
        assert instance.validator("X O O O X")==True
        assert instance.validator("O O O O O")==True
        assert instance.validator("X X O X A")==False
        assert instance.validator("")==True
