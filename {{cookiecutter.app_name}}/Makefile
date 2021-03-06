SHELL=/bin/bash
SHELLOPTS=errexit:pipefail

ENVDIR=env
ACTIVATE:=$(ENVDIR)/bin/activate

.PHONY:	clean

count=10

{% if cookiecutter.python_version == 3 %}
PYTHON_EXECUTABLE=python3
VIRTUALENV_EXECUTABLE=pyvenv
{% else %}
PYTHON_EXECUTABLE=python
VIRTUALENV_EXECUTABLE=virtualenv --no-site-packages
{% endif %}

requirements = requirements.txt requirements-dev.txt
virtualenv: $(ACTIVATE)
$(ACTIVATE): $(requirements)
	test -d $(ENVDIR) || $(VIRTUALENV_EXECUTABLE) $(ENVDIR)
	for f in $?; do \
		. $(ACTIVATE); pip install -r $$f; \
	done
	touch $(ACTIVATE)

dev: virtualenv
	. $(ACTIVATE); FLASK_CONFIG="../../conf/dev.py" $(PYTHON_EXECUTABLE) src/runserver.py

test: virtualenv
	. $(ACTIVATE); FLASK_CONFIG="../../conf/dev.py" py.test --cov {{cookiecutter.app_name}} src/tests.py

shell: virtualenv
	. $(ACTIVATE); FLASK_CONFIG="../../conf/dev.py" $(PYTHON_EXECUTABLE) src/manage.py shell

dummy: virtualenv
	. $(ACTIVATE); FLASK_CONFIG="../../conf/dev.py" $(PYTHON_EXECUTABLE) src/manage.py dummy -n $(count)

docs: virtualenv
	git submodule add git://github.com/kennethreitz/kr-sphinx-themes.git doc/_themes
	. $(ACTIVATE); make -C doc/ html
	open doc/_build/html/index.html

clean:
	rm -rf $(ENVDIR)
	rm -rf doc/_build/
