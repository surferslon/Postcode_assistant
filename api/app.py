import json
from functools import wraps

from flask import Flask, request

from postcode_assistant.handlers import CodeValidator, InputFormatter

app = Flask(__name__)


def request_validator(view):
    @wraps(view)
    def wrapper():
        code = request.json.get("code")
        if not code:
            return "Code is not defined", 400
        return view(code)

    return wrapper


@app.route("/print_numbers")
def print_numbers():
    return "\n".join(
        "ThreeFive" if (i % 3 == 0 and i % 5 == 0) else ("three" if i % 3 == 0 else ("five" if i % 5 == 0 else str(i)))
        for i in range(1, 101)
    )


@app.route("/format_input", methods=["POST"])
@request_validator
def format_input(code):
    formatter = InputFormatter(code)
    if formatter.output:
        return formatter.output
    return json.dumps({"errors": formatter.errors})


@app.route("/validate_code", methods=["POST"])
@request_validator
def validate_code(code):
    validator = CodeValidator(code)
    if validator.is_valid:
        return "Ok"
    return json.dumps({"errors": validator.errors})


@app.route("/post_code", methods=["POST"])
@request_validator
def post_code(code):
    formatter = InputFormatter(code)
    if not formatter.output:
        return json.dumps({"Input errors": formatter.errors}), 400
    validator = CodeValidator(formatter.output)
    if validator.is_valid:
        return f"The code {formatter.output} is valid"
    else:
        return json.dumps({"errors": validator.errors})
