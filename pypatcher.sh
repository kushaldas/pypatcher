#!/usr/bin/bash

yum install -y autoconf bluez-libs-devel bzip2  bzip2-devel db4-devel expat-devel findutils gcc-c++ gdbm-devel glibc-devel gmp-devel libffi-devel libGL-devel  libX11-devel  ncurses-devel net-tools openssl-devel pkgconfig readline-devel sqlite-devel tar tcl-devel tix-devel tk-devel valgrind-devel zlib-devel mercurial gdb patch

wget https://hg.python.org/cpython/archive/default.tar.bz2
tar -xjvf default.tar.bz2
cd cpython-default
wget http://kushal.fedorapeople.org/get_patch.py
chmod +x get_patch.py
./get_patch.py $1
patch -p1 < new_patch.patch
if [ $? -ne 0 ]
then
    echo "Patching failed."
    exit 1
fi
./configure --with-pydebug
if [ $? -ne 0 ]
then
    exit 1
fi
make -j6
if [ $? -ne 0 ]
then
    echo "Make failed."
    exit 1
fi
./python -m  test -w -j0
if [ $? -ne 0 ]
then
    echo "Tests failed."
    exit 1
fi
