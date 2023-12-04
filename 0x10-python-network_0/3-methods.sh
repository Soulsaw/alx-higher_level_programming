#!/bin/bash
# the bin
curl -siLX OPTIONS "$1" | grep -i 'Allow:' | cut -f2- -d' '
