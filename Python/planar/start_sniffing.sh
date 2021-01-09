#!/bin/sh
sigrok-cli -d fx2lafw:conn=1.42 -c samplerate=20k -C D0,D1 --continuous -P uart:baudrate=2400 -B uart | ./piper | python planar_decode.py
