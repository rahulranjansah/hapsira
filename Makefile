DOCKER_BASE_IMAGE := "hapsira:dev"
DOCKER_CONTAINER_NAME := "hapsira-dev"

docs:
	tox -e docs

image: Dockerfile pyproject.toml
	docker build \
	-t hapsira:dev \
	.

docker:
	docker run \
	-it \
	--rm \
	--name ${DOCKER_CONTAINER_NAME} \
	--volume $(shell pwd):/code \
	--user $(shell id -u):$(shell id -g) \
	${DOCKER_BASE_IMAGE} \
		bash

.PHONY: docs docker image
