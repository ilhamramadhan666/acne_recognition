# acne_recognition
For recognizing acnes and rosacea. Done. Deployed on Heroku.

```
https://ml-acne-recog.herokuapp.com/
```

return top label name (acne/rosacea type).

To get inference, send POST request to:

```
https://ml-acne-recog.herokuapp.com/process
```

with form-data body, key: img, type: file, and attach the image.

to run:
```
pip install -r requirements.txt
python main.py
```
to test, open another terminal, then:
```
python test.py
```
change the image path and the url if needed
