#!/bin/bash

cd /cpython
/usr/bin/sh ./configure --with-pydebug
make -j2
./python -m test -j2
