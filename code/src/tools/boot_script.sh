#!/bin/bash
DIR=/home/root/machine2014/code/src
export PYTHONPATH=$PYTHONPATH:$DIR
$DIR/tools/process_spawner.py P8_4 $DIR/spawn_collector.py 2>&1 >> $DIR/collector.log