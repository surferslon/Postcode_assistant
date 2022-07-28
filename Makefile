help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

run:  ## start the api server
	docker build -t postcodes_app .
	docker run --rm -d -p 8000:8000 -e PORT="8000" --name postcodes_app postcodes_app

stop:  ## stop the api server
	docker stop postcodes_app

print_numbers:  ## print numbers
	curl localhost:8000/print_numbers
	@printf "\n"

format_input: ## format input according to postcode format; syntax: format_input code=<code_to_validate>
	curl -X POST http://localhost:8000/format_input -H 'Content-Type: application/json' -d '{"code": "$(code)"}'
	@printf "\n"

validate_code:  ## validate code; syntax: validate_code code=<code_to_validate>
	curl -X POST http://localhost:8000/validate_code -H 'Content-Type: application/json' -d '{"code": "$(code)"}'
	@printf "\n"

post_code:  ## Format and validate code; syntax: post_code code=<code_to_post>
	curl -X POST http://localhost:8000/post_code -H 'Content-Type: application/json' -d '{"code": "$(code)"}'
	@printf "\n"

tests:  ## Run tests
	docker exec postcodes_app python -m pytest /usr/postcode_assistant/postcode_assistant/tests/ -s
