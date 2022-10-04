import streamlit as st
import openai

## openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_key = st.secrets["SECRET_KEY"]
## openai.api_key='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'

st.title('My Chefbot')
##subheader
st.subheader('Meet Your Personal Michelin Star Chef with OpenAI GPT-3')

##Image
## We need to import PIL module of python.
from PIL import Image
img=Image.open('chefbot_image.png')
st.image(img, caption='Chefbot')

## write
st.write('Being stuck in our own homes for months has given most people the motivation to invest in cookware and learn how to cook or bake by reading articles or watching YouTube videos. However, we all know baking the same loaf of bread 3 times can get old. Would not it be nice to be able to talk to a friend who is actually a famous chef or someone who worked at a Michelin star restaurant? That would be an awesome way to pick up new tips on baking the most scrumptious lemon cake or creamy artichoke soup. Using GPT-3 and Streamlit APP, you have the chance to talk to a Michelin star chef to ask questions on what you should cook next and even unlock a new way to bake a favorite snack such as scones.')


## prompt_text = st.text_input(label="Talk with your favourite chefbot.", value="Add here question")
prompt_text = st.text_input(label="Talk with your favourite chefbot.")

## start_sequence = "\nChef"
## restart_sequence = "\nPerson: "
## story="You are talking to a Michelin star chef who was mentored by Gordon Ramsay in the past. The chef has published 3 award winning cookbooks and had their own cooking channel on Youtube. You can ask for recipes based on the ingredients you buy at the store. \n\nPerson: Who are you?\nChef: I am a chef who recently became popular as an internet sensation during COVID-19. How may I help you today?\n\nPerson: How did your work become known to the public? \nChef: I started a blog and Youtube channel to show my dishes to the internet. \n\nPerson: How did you get noticed by Chef Gordon Ramsay?\nChef: I invited him to a VIP taste test at my Michelin star restaurant. That's when we met for the first time in person.\n\nPerson: What is your favorite Italian dessert? \nChef: Panna cotta is my favorite Italian dessert. \n\nPerson: What should I cook with milk? \nChef: If you want to add something sweet and creamy to your dishes, milk is a great ingredient choice. You can use it to make sauces, smoothies or desserts. For example, if you make a savory sauce, you can make it creamy by adding milk. If you make a smoothie, you can make it creamier by adding milk.\n\nPerson: What is your favorite drink?\nChef: I am a huge fan of Thai tea.",

response = openai.Completion.create(
  model="text-davinci-002",
  ## prompt="You are talking to a Michelin star chef who was mentored by Gordon Ramsay in the past. The chef has published 3 award winning cookbooks and had their own cooking channel on Youtube. You can ask for recipes based on the ingredients you buy at the store. \n\nPerson: Who are you?\nChef: I am a chef who recently became popular as an internet sensation during COVID-19. How may I help you today?\n\nPerson: How did your work become known to the public? \nChef: I started a blog and Youtube channel to show my dishes to the internet. \n\nPerson: How did you get noticed by Chef Gordon Ramsay?\nChef: I invited him to a VIP taste test at my Michelin star restaurant. That's when we met for the first time in person.\n\nPerson: What is your favorite Italian dessert? \nChef: Panna cotta is my favorite Italian dessert. \n\nPerson: What should I cook with milk? \nChef: If you want to add something sweet and creamy to your dishes, milk is a great ingredient choice. You can use it to make sauces, smoothies or desserts. For example, if you make a savory sauce, you can make it creamy by adding milk. If you make a smoothie, you can make it creamier by adding milk.\n\nPerson: What is your favorite drink?\nChef: I am a huge fan of Thai tea.",
  prompt=prompt_text,
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6
  #stop=["Person", "Chef"]
)

st.write('Chefbot Reply:')
st.write(response["choices"][0]["text"])


## video
vid=open('chatbot_vid.mp4', 'rb').read()
st.video(vid)

