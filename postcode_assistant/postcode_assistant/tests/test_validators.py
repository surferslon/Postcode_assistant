import pytest

from postcode_assistant.handlers import CodeValidator, InputFormatter


@pytest.mark.parametrize("test_code", ("EC1A 1BB", "W1A 0AX", "M1 1AE", "B33 8TH", "DN55 1PT"))
def test_validator_correct_codes(test_code):
    assert CodeValidator(test_code).is_valid is True


@pytest.mark.parametrize("test_code", ("n 1ZZ", "BBnD 19", "BIQq RZZ", "1IQQ 111", "0990 XXX"))
def test_validator_incorrect_codes(test_code):
    assert CodeValidator(test_code).is_valid is not True


@pytest.mark.parametrize(
    "test_input, expected_output",
    (
        ("e C1A1bb", "EC1A 1BB"),
        ("   w1a0ax      ", "W1A 0AX"),
        (" m1   1   A   e   ", "M1 1AE"),
        ("b338th", "B33 8TH"),
        ("D n55 1P T", "DN55 1PT"),
    ),
)
def test_formatter_correct_input(test_input, expected_output):
    output = InputFormatter(test_input).output
    assert output == expected_output
    assert CodeValidator(output).is_valid is True


@pytest.mark.parametrize("test_input", ("EC1A029384OIU1BB", "E"))
def test_formatter_incorrect_input(test_input):
    formatter = InputFormatter(test_input)
    assert formatter.errors == ["Code length is invalid"]
    assert formatter.output is None
