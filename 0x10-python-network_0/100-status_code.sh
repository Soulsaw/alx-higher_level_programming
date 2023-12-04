#!/bin/bash
# the bin
curl -L -s -X HEAD -w "%{http_code}" "$1"
