.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@grep -E '^\.PHONY: [a-zA-Z_-]+ .*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: install-dev ## Install development dependencies
install-dev:
	# Install wasienv locally
	python setup.py develop
	# Install pytest
	pip install pytest
	# Install and set the unstable SDK as defautl
	wasienv install-sdk unstable
	wasienv default-sdk unstable

.PHONY: test ## Test wasienv. Make sure you run `make install-dev` before.
test:
	pytest
