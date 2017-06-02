all: install clean

PROJECT_NAME=adminlte
PROJECT_HOME=~/project/$(PROJECT_NAME)
VENV_HOME=$(PROJECT_HOME)/virtualenv
SRC_HOME=.
STATIC_SRC=$(SRC_HOME)/static
MEDIA_SRC=$(SRC_HOME)/media
CONF_SRC=$(SRC_HOME)/conf

install: 
	@cp -rf $(SRC_HOME)/var $(PROJECT_HOME)/; \
	mkdir -p $(PROJECT_HOME)/var/run; \
	mkdir -p $(PROJECT_HOME)/var/www; \
	mkdir -p $(PROJECT_HOME)/var/lock; \
	mkdir -p $(PROJECT_HOME)/var/log; \
	if [ ! -d $(VENV_HOME) ]; \
	then \
		virtualenv $(VENV_HOME); \
#		$(VENV_HOME)/bin/pip install -U pip; \
	fi; \
	$(VENV_HOME)/bin/pip install -Ur requirement.txt; \
	touch $(PROJECT_HOME)/var/run/reload; \
	cp -rf $(STATIC_SRC) $(PROJECT_HOME)/var/www/;\
	cp -rf $(MEDIA_SRC) $(PROJECT_HOME)/var/www/;\
	cp -rf $(CONF_SRC) $(PROJECT_HOME)/;\
	cp -rf manage.py $(PROJECT_HOME)/;

clean:
	@rm -rf adminlte.egg-info build dist
