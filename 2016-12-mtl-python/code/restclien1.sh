#!/bin/bash
export no_proxy='127.0.0.1'
curl http://127.0.0.1:5000/voltage
curl http://127.0.0.1:5000/turn_on -d "data=" -X PUT
curl http://127.0.0.1:5000/voltage -d "data=4" -X PUT
curl http://127.0.0.1:5000/voltage
