# Variables
APP=dash/dash_word_cloud.py
REQS=requirements.txt

install: 
	pip install -r $(REQS)

run: install
	pyhton3 $(APP)
