#!/bin/bash
curl -H "Content-Type: application/json" -XPOST --data "@post.json" http://localhost:5000/bitbucket/test?token=dev
