echo "deploy success"
cd ../myslackbot
pip install -r requirements.txt
nohup python3 app.py &
