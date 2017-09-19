### Makefile --- 

## Author: shell@xps13
## Version: $Id: Makefile,v 0.0 2017/09/19 08:43:54 shell Exp $
## Keywords: 
## X-URL: 

all: test

test:
	python -m unittest discover -p "*.py"


### Makefile ends here
