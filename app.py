from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           age_mapping=age_mapping, 
                           gender_mapping=gender_mapping,
                           country_mapping=country_mapping,
                           highest_deg_mapping=highest_deg_mapping,
                           code_experience_mapping=code_experience_mapping,
                           current_title_mapping=current_title_mapping,
                           company_size_mapping=company_size_mapping)

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

if __name__ == '__main__':
    app.run(debug=True)