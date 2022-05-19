#!/bin/bash

curl -sI "$1" | grep Content-Length: | tr " " "\n" | tail -1