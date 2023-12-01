#!/bin/bash
# the bin
curl -s -w "%{http_code}" "$1"
