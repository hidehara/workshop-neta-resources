FROM lambci/lambda:build-python3.8

ADD . .

CMD pip3 install -r requirements.txt -t /var/task/site-packages && \
  zip -9 deploy_package.zip lambda_function.py && \
  cd site-packages && \
  zip -r9 ../deploy_package.zip *
