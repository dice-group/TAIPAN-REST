build:
	docker build -t taipan-rest .

run:
	docker run -it --rm -p 80:5000 --volume $(shell pwd)/taipanserver:/taipanserver taipan-rest
