#!/bin/bash
# the bin
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
