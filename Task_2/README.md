## Task_2

Since you have prepared the data which can be used by students to study translation, now is the time 
for integrating this feature in the app. The frontend engineer needs 10 translation sentence pair from 
a data upon a request sent to backend.

Being a data scientist of a startup and a small team, you take care of API's related to machine learning 
models. Please help the team by writing a Flask-based API which returns 10 translation pairs from the 
dataset.

## Dependencies
- Python 3.9 or later
- PyCharm

## Quick Start
### Local deployment
- Create a Virtual conda environment: ```conda create -n multilingo_env_2 python=3.9```
- Activate the conda environment: ```conda activate multilingo_env_2```
- Installing the required packages: ```pip install -r requirements.txt```
- Run the file: ``` python app.py```
### Docker deployment
- Build a Docker image: ```docker build -t multilingo_api .```
- Run the container: ```docker run -p 8080:8080 multilingo_api```
## Endpoints
    1. GET /api/v1/status
    
	    - returns appropriate status code of API

    2. GET /api/v1/sentences
    
	    - returns 10 sentences in a list
    
	    - returns appropriate status code
        
        - response: jsonify(ten_sentence)