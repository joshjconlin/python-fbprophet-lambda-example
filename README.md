 to run:
 
 docker run --rm -it -v "${PWD}":/var/task lambci/lambda:build-python3.6 bash
 . venv/bin/activate
   
 python lambda_handler.py 