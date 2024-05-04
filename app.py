from flask import Flask, request, render_template
import joblib
import joblib
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from sklearn.compose import ColumnTransformer

app = Flask(__name__)
model = joblib.load('./Recommender.pkl')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = pd.DataFrame([{'Security': ("Low" if request.form['security'] == "Low" else "High"),
                          'Runtime Efficiency': request.form['efficiency'],
                          'Ease of Implementation': 'Moderate',
                          'Use Cases': request.form['usecase'],
                          'Flexibility': request.form['flexibility'],
                          'Scalability': request.form['scalibility']}])
    
    # Implement logic here to determine the best algorithm
    # Placeholder response
    cols = data.columns.tolist()
    # cols.remove('Algorithms')
    column_transformer = ColumnTransformer(
		[("one_hot_encoder", OneHotEncoder(), cols)],
		remainder='passthrough'  # this leaves all other columns in their original form
	)
    base_data = pd.read_csv("Data.csv")
    X = column_transformer.fit_transform(base_data.drop('Algorithms', axis=1))
    # model = joblib.load("Recommender.pkl")
    new_data_transformed = column_transformer.transform(data)
    recommended_algorithm_index = model.predict(new_data_transformed)[0]
    return render_template('answer.html', Algorithm=recommended_algorithm_index)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000 ,debug=True)
