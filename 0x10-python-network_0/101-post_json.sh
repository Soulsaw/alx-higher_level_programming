#!/bin/bash
# the bin
curl -sX POST "$1" -H 'Content-Type: application/json' -d @"$2"
