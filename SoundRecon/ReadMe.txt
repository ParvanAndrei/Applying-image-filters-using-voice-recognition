// Intrusctiuni de utilizare
// Semnul ">" inseamna comanda executata in terminal
// Doc python SpeechRecognition
// https://pypi.org/project/SpeechRecognition/
// set microfon doc
// https://iotbytes.wordpress.com/connect-configure-and-test-usb-microphone-and-speaker-with-raspberry-pi/

1. Activare virtual environment:
>source /home/pi/Desktop/SoundRecon/venv/bin/activate

2. Exemplu de rulare speachrecognition
>python3 -m speech_recognition

// link util pentru USB camera handle: 
// https://raspberrypi-guide.github.io/electronics/using-usb-webcams

// link util instalare openCV
// https://raspberrypi-guide.github.io/programming/install-opencv.html

3. Rulare sesiune VNC pe Raspbery:
>vncserver :33 -geometry 1920x1080 
// de verificat daca nu ruleaza deja

4. Speaker test
>speaker-test -t wav -c 2

4. Rulare program (pentru a rula programul ai nevoie ori sa te conectezi print-o sesiune VNC 
la raspberrypi ori sa fii direct in raspberrypi)
>cd /home/pi/Desktop/SoundRecon
>python3 main.py




