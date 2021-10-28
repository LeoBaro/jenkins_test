import pytest
from SampleProject.utils import how_many_seconds

class TestUtils:

    @pytest.mark.parametrize("test_input,expected_seconds", 
    [
        ({"days":1,"hours":1,"minutes":1,"seconds":0}, 90060),
        ({"days":1,"hours":1,"minutes":1,"seconds":10}, 90070)
    ])

    def test_how_many_seconds(self, test_input, expected_seconds):
        
        seconds = how_many_seconds(test_input["days"],test_input["hours"],test_input["minutes"],test_input["seconds"])
        assert seconds == expected_seconds
