#!/bin/bash
# Get the size in bytes of the response header
curl -s "$1" | wc -c
