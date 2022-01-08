from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from six import print_
from analyzer.models import Feedback

import pandas as pd

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Dense, Dropout, SpatialDropout1D
from tensorflow.keras.layers import Embedding

df = pd.read_csv(r"analyzer/Tweets.csv")
tweet_df = df[['text','airline_sentiment']]
tweet_df = tweet_df[tweet_df['airline_sentiment'] != 'neutral']
sentiment_label = tweet_df.airline_sentiment.factorize()
tweet = tweet_df.text.values
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(tweet)
vocab_size = len(tokenizer.word_index) + 1
encoded_docs = tokenizer.texts_to_sequences(tweet)
padded_sequence = pad_sequences(encoded_docs, maxlen=200)
embedding_vector_length = 32
model = Sequential() 
model.add(Embedding(vocab_size, embedding_vector_length, input_length=200) )
model.add(SpatialDropout1D(0.25))
model.add(LSTM(50, dropout=0.5, recurrent_dropout=0.5))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid')) 
model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy'])   
history = model.fit(padded_sequence,sentiment_label[0],validation_split=0.2, epochs=1, batch_size=32)
def predict_sentiment(text):
    tw = tokenizer.texts_to_sequences([text])
    tw = pad_sequences(tw,maxlen=200)
    prediction = int(model.predict(tw).round().item())
    print("Predicted label: ", sentiment_label[1][prediction])
    return sentiment_label[1][prediction]


def home(request):
    if request.method == "POST":
        # test_sentence1 = "This was the best ride ever."
        # predict_sentiment(test_sentence1)
        name = request.POST.get('namef')
        email = request.POST.get('emailf')
        age = request.POST.get('agef')
        role = request.POST.get('rolef')
        question1 = request.POST.get('q1')
        question2 = request.POST.get('q2')
        question3 = request.POST.get('q3')
        question4 = request.POST.get('q4')
        new_feedback = Feedback(name=name,email=email,age=age,role=role,q1=question1,q1s=predict_sentiment(question1),q2=question2,q2s=predict_sentiment(question2),q3=question3,q3s=predict_sentiment(question3),q4=question4,q4s=predict_sentiment(question4))
        print(new_feedback)
        new_feedback.save()
        return HttpResponse("<h1>Thanks for your valuable time</h1>")
    else:
        return render(request, "index.html")
