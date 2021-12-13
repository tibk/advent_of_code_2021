APP_NAME = $(shell python setup.py --name)
VENV_PREFIX = $(shell echo $(APP_NAME) | tr [a-z] [A-Z])
VENV_NAME = py38-$(APP_NAME)
VERSION = $(shell python setup.py --version)
ENV = dev


PIP = $(WORKON_HOME)/$(VENV_NAME)/bin/pip3
PYTHON = $(WORKON_HOME)/$(VENV_NAME)/bin/python3
VIRTUALENV = $(PYENV_ROOT)/versions/3.8.0/bin/virtualenv


LINT_OPTION = --max-line-length 180 --ignore _ --import-order-style=edited --application-import-names=common,config,scripts,tests,utils 


init: init-venv update-venv init-runtime


init-venv:
	test -d $(WORKON_HOME)/$(VENV_NAME) || $(VIRTUALENV) $(WORKON_HOME)/$(VENV_NAME)


init-runtime:  ## Initialize application vendors dependencies
	$(PIP) install -Ur requirements.txt


update-venv:
	$(PIP) install -U pip

deinit:
	rm -rf $(WORKON_HOME)/$(VENV_NAME)


lint:
	$(WORKON_HOME)/$(VENV_NAME)/bin/black --check .


clean:
	true || true


help: ## Show this help.
	@grep -E "^[^.][a-zA-Z_-]*:" Makefile | awk -F '[:#]' '{print $$1, ":", $$NF}' | sort | column -t -s:


.SILENT: deinit init init-venv init-runtime update-venv lint 
.PHONY: deinit init init-venv init-runtime update-venv lint 
