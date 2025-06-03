#!/bin/bash

git init
git add *
git commit -m "first-commit"
git branch -M main
git remote add origin https://github.com/Darz2/Summer_School_polimi.git
git push -u origin main