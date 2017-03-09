#!/bin/bash
curl -H "Content-Type: application/json" -XPOST --data "@post.json" http://localhost:5000/git/test?token=dev1
