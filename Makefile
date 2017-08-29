build-dev:
	docker build -t taipan-rest --file Dockerfile-dev .

run-dev:
	docker run -it --rm -p 80:5000 \
	--volume $(shell pwd)/../taipan-lib:/taipan-lib \
	--volume $(shell pwd)/taipanserver:/taipanserver \
	--volume $(shell pwd)/../foxpy:/foxpy \
	--volume $(shell pwd)/../agdistispy:/agdistispy taipan-rest

build:
	docker build -t taipan-rest .

run:
	docker run -it --rm -p 80:5000 taipan-rest
