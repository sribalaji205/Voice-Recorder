from flask import Flask,render_template,redirect,url_for
from threading import Timer
import webbrowser
import speech_recognition as sr
import os
import sys
from pydub import AudioSegment

def speech(recognizer,audio):
      i=1
      while os.path.exists("road%s.mp3"%i):
            i+=1
      if not os.path.exists("road%s.mp3"%i):
            aud=open('road%s.wav'%i,'ab')
            aud.write(audio.get_wav_data())
            sound=AudioSegment.from_file("road%s.wav"%i,format="raw",frame_rate=44100,channels=2,sample_width=2)
            sound.export("road%s.mp3"%i,format="mp3")
            aud.close()
      else:
            i+=1
            aud=open('road%s.mp3'%i,'ab')
            aud.write(audio.get_wav_data())
            sound=AudioSegment.from_file("road%s.wav"%i,format="raw",frame_rate=44100,channels=2,sample_width=2)
            sound.export("road%s.mp3"%i,format="mp3")
            aud.close()
      os.remove("road%s.wav"%i)

r = sr.Recognizer()
mic = sr.Microphone()
         
app=Flask(__name__)
@app.route('/')
def home():
      return render_template("spchrecog.html")


@app.route('/record/')
def record():
      with mic as source:
            audio1 = r.listen(source)
      speech(r,audio1)
      stop_listening=r.listen_in_background(mic,speech)
      stop_listening()
      return redirect(url_for("home"))


@app.route("/stop/")
def stop():
      return redirect(url_for("home"))
      
def open_browser():
      webbrowser.open_new('http://127.0.0.1:2000/')

if __name__ == "__main__":
      Timer(0.5,open_browser).start();
      app.run(port=2000)


      
            
            
            
      
