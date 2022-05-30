#!/bin/bash
echo "Packing lambda and libraries"
/usr/bin/python3.8 -m virtualenv tmp_venv
source tmp_venv/bin/activate
pip install -r requirements.txt
cp -R lambda_function.py /usr/lib/x86_64-linux-gnu/libpq.so.5 tmp_venv/lib/python3.8/site-packages/
cd tmp_venv/lib/python3.8/site-packages/
zip -r lambda_function.zip *
cd -
cp tmp_venv/lib/python3.8/site-packages/lambda_function.zip .
deactivate
rm -R tmp_venv