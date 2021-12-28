# Json-Validator

A custom Json Validator, validates the message schema to filter missing missing fields and mismatch field datatypes against defined schema.


## Directory Structure

```
.
├── data
│   └── input.json
│   └── report.csv
├── Dockerfile
├── lib
│   ├── __init__.py
│   ├── logger.py
│   └── utils.py
├── main.py
├── README.md
├── requirements.txt
├── setup.py
└── src
    ├── __init__.py
    ├── report.py
    └── validator.py
```

- `Json-Validator` contains the project directory
- `Json-Validator\main.py` is script consuming `Report` class
- `Json-Validator\src\report.py` is the script consuming `Report` class with associated methods
- `Json-Validator\src\validator.py` is the script consuming `Validator` class with associated methods
- `Json-Validator\lib\utils.py` holds utilites functions that assists in file operations
- `Json-Validator\lib\logger.py` module for logging information of the operations
- `Json-Validator\data\input.json` holds data file `input.json` to process
- `Json-Validator\data\report.csv` holds data file `report.csv`, output file of the process
- `Json-Validator\Dockerfile\` is a docker file script
- `Json-Validator\screenshot\` is a directory with output screenshots on terminal

## Dataset

- Dataset file is in data directory, and is in json format.
- Datasets

  - `input.json` : json input data set file
  - `report.csv` : report file is generated at the end of process completion

## Instruction to use

### Without Docker

- Go to the project directory `Json-Validator`
- Run the `pip install -r requirements.txt`
- Run the `pip install -e .`
- Run the script `main.py`

  ```python
  python main.py
  ```

### With Docker

```python
docker build -t <image-name> .
docker run <image-name>
```

## output

- once the process is complete, all the results will be added to `Json-Validator/data/report.csv` file as:

```text
               EventName  EventDate EventCount
      submissionSuccess  2018-01-30          1
  registrationInitiated  2018-02-03          1
      submissionSuccess  2018-02-27          1
  registrationInitiated  2018-01-03          1
      submissionSuccess  2019-02-27          1
  registrationInitiated  2019-01-03          2
```
