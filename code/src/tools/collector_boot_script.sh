#!/bin/bash
DIR=/home/root/machine2014/code/src
export PYTHONPATH=$PYTHONPATH:$DIR
$DIR/main_collector.py 2>&1 >> $DIR/collector.log
while [ $? -ne 0 ]; do
  echo "Error: main_collector.py crashed, trying again"
  sleep 10
  $DIR/main_collector.py 2>&1 >> $DIR/collector.log
done