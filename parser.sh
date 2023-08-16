#!/bin/bash

INPUT_PATH="logs/tob-stt-v1/"
OUTPUT="./logs/tob_v1_dataset"

rm $OUTPUT

echo "user,question,answer" >> $OUTPUT

for log_file in `ls $INPUT_PATH`
do
  python3 parser.py "$INPUT_PATH/$log_file" >> $OUTPUT
done

