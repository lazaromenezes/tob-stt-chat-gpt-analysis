from python:slim

copy . .

run pip install -r requirements.txt

entrypoint ["python", "extractor.py"]
