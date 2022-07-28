# UK Codes validator

## Requirements
- Docker

## Description
The project consists of two parts, api server and validation library which is installed separately.
<br>
Once the project is cloned use the following makefile commands to run and test the app

- `make run` <br> Start the container with the app and validation library.
- `make stop` <br> Stop the app container
- `make print_numbers` <br> Print numbers according to the task N1
- `make format_input code=<code_to_test>`<br>
Format a string according to the postcode rules. <br>
Example: `make format_input code="  d3 R7D   r  "`
- `make validate_code code=<code_to_test>`<br>
Validate a code. <br>
Example: `make post_code code="D3R 7DR"`
- `make post_code code=<code_to_test>`<br>
Format and validate a code. <br>
Example: `make post_code code="  d   3r7d r"`
- `make tests` <br> Run all available tests
- `make help` <br> List available makefile commands
