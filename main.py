from flask import Flask
import subprocess
import time
import os
from threading import Thread

app = Flask(__name__)

scripts = [
    'script1.py', 'script2.py', 'script3.py', 'script4.py', 'script5.py',
    'script6.py', 'script7.py', 'script8.py', 'script9.py', 'script10.py',
    'script11.py', 'script12.py', 'script13.py', 'script14.py', 'script15.py',
    'script16.py', 'script17.py', 'script18.py', 'script19.py', 'script20.py',
    'script21.py', 'script22.py'
]

script_status = {script: "Not started" for script in scripts}

def run_scripts():
    while True:
        for script in scripts:
            if os.path.exists(script):
                try:
                    script_status[script] = "Running"
                    subprocess.run(['python', script], check=True)
                    script_status[script] = "Success"
                except subprocess.CalledProcessError as e:
                    script_status[script] = f"Error: {str(e)}"
                except FileNotFoundError:
                    script_status[script] = "File not found"
            else:
                script_status[script] = "File not found"
        
        time.sleep(15)

@app.route('/')
def status_page():
    status_html = "<h1>Script Status</h1>"
    status_html += "<table border='1'><tr><th>Script</th><th>Status</th></tr>"
    
    for script, status in script_status.items():
        status_html += f"<tr><td>{script}</td><td>{status}</td></tr>"
    
    status_html += "</table>"
    return status_html

if __name__ == '__main__':
    # Start the script running thread
    script_thread = Thread(target=run_scripts)
    script_thread.daemon = True
    script_thread.start()
    
    # Start Flask server
    app.run(host='0.0.0.0', port=8080)
