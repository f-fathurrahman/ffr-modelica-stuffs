#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo
  echo "ERROR"
  echo "Need exactly one parameter: Modelica source file in *.mo extension"
  echo "Example: ./build.sh myfile.mo"
  echo
  exit 1
fi

BASNAM=`basename $1 .mo`

if [ $BASNAM == "$1" ]; then
  echo "Error: file name does not have *.mo"
	exit 1
fi

omc -s -d=initialization $1


# Edit Makefile
# Make sure that the extension in .exe so that it can be used in gitignore file
sed -i "s/EXEEXT=/EXEEXT=.exe/g" $BASNAM.makefile
make -f $BASNAM.makefile

