import os
import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_ticket_reply(ticket_title, ticket_description):
    prompt = f"""
    You are a customer support assistant. 
    A user submitted this ticket:

    Title: {ticket_title}
    Description: {ticket_description}

    Write a short, polite reply in plain text. 
    - No subject line
    - No greetings like "Hi [User Name]"
    - No signature
    - Keep it minimal and direct
    """
    response = model.generate_content(prompt)
    return response.text.strip()

