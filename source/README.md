# Building Your Challenge

To be run on a machine with a webcam connected.
Does NOT work on WSL, even with the webcam passed through usbpid.

Run the program on the machine:
```
python3 -m pip install -r requirements.txt
python3 main.py
```

Program runs indefinitely. There is a cooldown between two link requests (5 sec, can adjust).

