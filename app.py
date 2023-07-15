from flask import Flask, render_template, send_file, request
import subprocess

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/datascience')
def datascience():
    return render_template('datascience.html')


@app.route('/fullstack')
def fullstack():
    return render_template('fullstack.html')


@app.route('/devops')
def devops():
    return render_template('devops.html')


@app.route('/cloud')
def cloud():
    return render_template('cloud.html')


@app.route('/datascience.json')
def servedatascience_json():
    return send_file('templates/datascience.json', mimetype='application/json')


@app.route('/fullstack.json')
def servefullstack_json():
    return send_file('templates/fullstack.json', mimetype='application/json')


@app.route('/cloud.json')
def servecloud_json():
    return send_file('templates/cloud.json', mimetype='application/json')


@app.route('/devops.json')
def servedevops_json():
    return send_file('templates/devops.json', mimetype='application/json')


@app.route('/download', methods=['GET', 'POST'])
def download():
    job_search = ""

    # Determine job search parameter based on the HTML file
    html_file = request.form.get('html_file')
    if html_file == 'datascience.html':
        job_search = "data science"
    elif html_file == 'fullstack.html':
        job_search = "full stack"
    elif html_file == 'devops.html':
        job_search = "dev ops"
    elif html_file == 'cloud.html':
        job_search = "cloud engineer"
    # Add more conditions for other HTML files if needed

    # Run the web scraping script with the job search parameter
    subprocess.run(['python', 'main.py', job_search], shell=True)

    # Return the generated CSV file for download
    return send_file('trial.csv', as_attachment=True, cache_timeout=0)


if __name__ == '__main__':
    app.run(debug=True)
