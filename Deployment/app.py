import pickle
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

with open("model_deposito_all_in_one.pkl", "rb") as file:
    loaded_objects = pickle.load(file)

model = loaded_objects['model']

FEATURES = [
    'age', 'default', 'housing', 'loan', 'campaign', 'pdays', 'previous',
    'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'contact_quarter',
    'emp.var.rate_bin', 'cons.price.idx_bin', 'cons.conf.idx_bin',
    'euribor3m_bin', 'nr.employed_bin', 'job_admin.', 'job_blue-collar',
    'job_entrepreneur', 'job_housemaid', 'job_management', 'job_retired',
    'job_self-employed', 'job_services', 'job_student', 'job_technician',
    'job_unemployed', 'marital_divorced', 'marital_married',
    'marital_single', 'contact_cellular', 'contact_telephone',
    'poutcome_failure', 'poutcome_nonexistent', 'poutcome_success',
    'education_basic.4y', 'education_basic.6y', 'education_basic.9y',
    'education_high.school', 'education_illiterate',
    'education_professional.course', 'education_university.degree',
    'month_apr', 'month_aug', 'month_dec', 'month_jul', 'month_jun',
    'month_mar', 'month_may', 'month_nov', 'month_oct', 'month_sep',
    'day_of_week_fri', 'day_of_week_mon', 'day_of_week_thu',
    'day_of_week_tue', 'day_of_week_wed', 'age_bin_Dewasa',
    'age_bin_Dewasa Tua', 'age_bin_Lansia', 'age_bin_Muda', 'age_bin_Tua'
]

LABEL = ['No', 'Yes']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # Define categorical columns here
    categorical_cols = ['job', 'marital', 'education', 'default', 
                        'housing', 'loan', 'contact', 'month', 
                        'poutcome']
    
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)

                data = pd.read_csv(filepath)

                for col in categorical_cols:
                    if col in data.columns:
                        data[col] = data[col].astype('category')

                predictions = model.predict(data)

                data['Prediction'] = [LABEL[pred] for pred in predictions]

                return render_template('predict.html', tables=[data.to_html(classes='data')], titles=data.columns.values)

        input_data = {key: float(request.form.get(key, 0)) for key in FEATURES}

        new_data = pd.DataFrame([input_data])
        for col in categorical_cols:
            if col in new_data.columns:
                new_data[col] = new_data[col].astype('category')

        res = model.predict(new_data)
        result_label = LABEL[res[0]]

        return render_template('predict.html', result=result_label)

    return redirect(url_for('index'))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
