import streamlit as st
import openai
import speech_recognition as sr

import os

mic=sr.Microphone()
r=sr.Recognizer()
key="XXXXXXXXXX API KEYXXXXXXXXXXXXX"

os.environ["OPENAI_API_KEY"]=key
openai.api_key=os.getenv("OPENAI_API_KEY")


role=st.text_input("wie soll ich antworten, genau , kurz und knapp oder detailiert welcher stil ")
# question=st.text_input("Stell deine Frage?")

def get_recognized():
    
    with mic as source:
        global query,messages
        audio=r.listen(source)
        query=r.recognize_google(audio,language="de-DE")
        print(query)
      
        messages=[
    {"role":"system","content":role},
    {"role":"user","content":query}
    ]

    



        output=openai.ChatCompletion.create(

        model="gpt-3.5-turbo",
        # model="text-davinci-003",
        messages=messages,
        temperature=0.8,
        frequency_penalty=0,
        presence_penalty=0,
        max_tokens=1000


        )

        print(output)



        st.write(output.choices[0].message.content)



st.button("Frag mich....",on_click=get_recognized)

exit()

