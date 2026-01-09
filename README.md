# flask_demo
## Start the WSGI server
there are **2** ways to start the WSGI server.
### Run python file directly
```python
python app.py
```
### Run through Dockerfile
```bash
# 1 start your virtual machine
colima start
# 2 build docker image
bash build.sh
# 3 run docker image
docker run -p 5001:5001 flask-math-api
# 4 stop virtual machine
colima stop
```
## Use the WSGI server
you can then run the following example command on any other device that's on the same local network as your computer.
```bash
curl -X POST http://YOUR_LAN_IP_ADDRESS/api/math/square -H "Content-Type: application/json" -d '{"n": 8}'
```