# Variables
APP=dash/dash_word_cloud.py
REQS=requirements.txt

install: 
	pip install -r $(REQS)

run: install
	/home/codespace/.python/current/bin/python3 $(APP)

test : 
	pip install pytest==7.0.1 
	pytest -v

delete :
	rm -rf data 

all : install run 