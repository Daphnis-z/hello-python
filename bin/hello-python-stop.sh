#! /bin/bash
# -*- sh -*-

# shellcheck disable=SC2009
ps -ef | grep hello-python | grep -v grep | awk '{print "kill " $2}' | sh
