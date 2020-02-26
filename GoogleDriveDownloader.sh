#!/bin/bash
fileid="1RObmCDPeQ1Lg-V6u7dT02Pf0qH-QMcTp"
filename="blur_dataset.zip"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}