#!/bin/bash

for i in {0..9999}
do
    printf "%s %04d\n" "formattest" "$i"
done
