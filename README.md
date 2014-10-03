To create the certificate:

openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem


To run:

ipython notebook --no-browser --ip=10.65.82.56 --port 9999 --certfile=mycert.pem --profile notebook_web


