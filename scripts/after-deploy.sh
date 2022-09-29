echo "deploy success"
cd /home/ubuntu/myslackbot
pip install -r requirements.txt
nohup python3 app.py &
