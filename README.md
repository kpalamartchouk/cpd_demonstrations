# Demonstrations for CPD Courses
## Harmonics beating
## Cross-correlation of binary sequences

## Running the presentations
### Running the presentation from a notebook server:

1.  To create the certificate:

    ```
    openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem
    ```

2.  Create new ipython profile for serving over the network:
    ```
    ipython profile create notebook_web
    ```
    Now edit `~/.ipython/profile_notebook_web/ipython_notebook_config.py` to add the line
    ```
    c.NotebookApp.password = u'sha1:2573f21f4b80:42a3eae8bd6c98a9112b4d61458762342342f7ff'
    ```
    where the sha1 hash is produced by:
    ```python
    from IPython.lib import passwd
    passwd()
    ```

3.  Running the server (use the correct IP address and port):
    ```
    ipython notebook --no-browser --ip=10.65.82.56 --port 9999 --certfile=mycert.pem --profile notebook_web
    ```

### Running the presentation from a pre-created html:

1.  Convert the notebook to html:
    ```
    ipython nbconvert Gold_Code_Correlations.ipynb --to=slides
    ```

2.  Make sure there is a copy of [reveal.js](https://github.com/hakimel/reveal.js) next to the resulting html:
    ```
    git clone https://github.com/hakimel/reveal.js.git
    ```

3.  Give access to all that by http:
    ```
    python -m SimpleHTTPServer 8000
    ```

