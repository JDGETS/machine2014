#!/bin/bash
DIR=/home/root/machine2014/code/src
export PYTHONPATH=$PYTHONPATH:$DIR
$DIR/main_camion.py 2>&1 >> $DIR/collector.log
