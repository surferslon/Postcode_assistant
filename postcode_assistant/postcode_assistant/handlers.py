import re
from typing import Union


class CodeValidator:
    code: str
    is_valid: bool
    errors: list

    def __init__(self, code):
        self.code = code
        self.errors = []
        self.validate_code()
        self.is_valid = not self.errors

    def validate_code(self):
        try:
            outward_code, inward_code = self.code.split(" ")
        except ValueError:
            self.errors.append("Code format doesn't have space")
            return
        if not re.match("^[A-Z]{1,2}[0-9][A-Z0-9]?", outward_code):
            self.errors.append("outward code is invalid")
        if not re.match("^[0-9][A-Z]{2}$", inward_code):
            self.errors.append("inward code is invalid")


class InputFormatter:
    input: str
    output: Union[str, None] = None
    errors: list

    def __init__(self, code):
        self.input = code
        self.errors = []
        self.format_input()

    def format_input(self):
        code = self.input.strip().upper()
        code = re.sub(" +", "", code)
        if not (4 < len(code) < 8):
            self.errors.append("Code length is invalid")
            return
        incode_len = 3
        outcode_len = len(code) - incode_len
        code = " ".join([code[:outcode_len], code[outcode_len:]])
        self.output = code
