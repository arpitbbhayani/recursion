lint:
	autopep8 *.py  --in-place --aggressive --max-line-length 80
	pylint *.py
