from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
import speech_recognition as sr

# Create your views here.


def home(request):
    if request.method == "POST":
        return HttpResponse("galat reload")
    #     # initialize the recognizer
    #     r = sr.Recognizer()
    #     with sr.Microphone() as source:
    #         # read the audio data from the default microphone
    #         audio_data = r.record(source, duration=20)
    #         print("Recognizing...")
    #         # convert speech to text
    #         text = r.recognize_google(audio_data)
    #         print(text)
    #     return render(request, "index.html")
    else:
        return render(request, "index.html")
