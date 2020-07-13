#!/usr/bin/env bash
ROOT_DIR=${1}
for d in $(ls ${ROOT_DIR});
do
    echo create ${d} dataset
    poetry run kaggle d create  --dir-mode tar --public -p ${ROOT_DIR}/${d}
done;
