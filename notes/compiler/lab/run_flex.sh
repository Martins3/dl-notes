#!/bin/bash
flex learn-flex-$1.l
clang lex.yy.c -lfl
./a.out
