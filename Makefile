# Variables
APP=dash/dash_word_cloud.py
REQS=requirements.txt

install: 
	pip install -r $(REQS)

run: install
	/home/codespace/.python/current/bin/python3 $(APP)

delete :
	rm -rf data 

all : install run 
