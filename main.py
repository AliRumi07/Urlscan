from flask import Flask
import subprocess
import time
import os
import threading

app = Flask(__name__)

# Global variable to control script execution
running = False
thread = None

def run_scripts():
    global running
    scripts = [
        'script1.py',
        'script2.py',
        'script3.py',
        'script4.py',
        'script5.py',
        'script6.py',
        'script7.py',
        'script8.py',
        'script9.py',
        'script10.py',
        'script11.py',
        'script12.py',
        # Add more scripts here as needed
    ]
    
    while running:
        for script in scripts:
            if not running:
                break
                
            if os.path.exists(script):
                try:
                    print(f"Running {script}")
                    subprocess.run(['python', script], check=True)
                    print(f"Finished running {script}")
                except subprocess.CalledProcessError as e:
                    print(f"Error running {script}: {e}")
            else:
                print(f"Script {script} not found")
                
            # Wait 15 seconds before running next script    
            time.sleep(15)
            
        print("Completed one round, starting again...\n")

@app.route('/start')
def start():
    global running, thread
    if not running:
        running = True
        thread = threading.Thread(target=run_scripts)
        thread.start()
        return 'Scripts started running'
    return 'Scripts are already running'

@app.route('/stop')
def stop():
    global running
    running = False
    return 'Scripts stopped'

@app.route('/status')
def status():
    global running
    return 'Running' if running else 'Stopped'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
