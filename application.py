## same file as app.py but with the name changed to application.py for python.config file to recognize it as the entry point
## for the application to be deployed on the aws container

from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from src.pipelines.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return render_template('index.html')


# This will get the data from the server and call the prediction pipeline and get the results 
@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html') 
    
    # When the post method is hit, we woould like to get the data from the form where the user has posted the data
    else:
        # Creating an object of CustomData class by getting the data from the submitted form ; this will run only if the data obtained
        # \n follows the data types as mentioned in the CustomData class
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )

        pred_df = data.get_data_as_data_frame()

        
        predict_pipeline = PredictPipeline()

        results = predict_pipeline.predict(pred_df)

        return render_template('home.html', results=results[0])


if __name__=='__main__':
    # it will map to 127.0.0.1 default ip address, default port is 5000
    app.run(host="0.0.0.0")
    # while deploying "deploy = true" should be removed