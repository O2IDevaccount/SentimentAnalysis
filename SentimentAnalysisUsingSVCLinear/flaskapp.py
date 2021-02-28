from flask import Flask, render_template, request, url_for
from wtforms import Form, TextAreaField, validators
import pickle
import sqlite3
import os
import numpy as np
import joblib
loaded_model=joblib.load(r"models\model.pkl")
loaded_stop=joblib.load(r"models\stopwords.pkl")
loaded_vec=joblib.load(r"models\vectorizer.pkl")

app = Flask(__name__)
def classify(document):
	label = {0: 'positive', 1: 'negative'}
	X = loaded_vec.transform([document])
	y = loaded_model.predict(X)[0]
	proba = np.max(loaded_model.predict_proba(X))
	return label[y], proba
class ReviewForm(Form):
	moviereview = TextAreaField('',[validators.DataRequired(),validators.length(min=15)])

@app.route('/')
def index():
	form = ReviewForm(request.form)
	return render_template('reviewform.html', form=form)
@app.route('/results', methods=['POST'])
def results():
	form = ReviewForm(request.form)
	if request.method == 'POST' and form.validate():
		review = request.form['moviereview']
		y, proba = classify(review)
	return render_template('results.html',content=review,prediction=y,probability=round(proba*100, 2))
	return render_template('reviewform.html', form=form)
if __name__ == '__main__':
 app.run(debug=True)
