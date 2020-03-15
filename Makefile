main:
	@pipenv run python3 src/main.py

dependencies:
	@docker-compose up -d

clean:
	@pipenv --rm

.PHONY: main dependencies clean
