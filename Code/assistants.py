import streamlit as st
import os
from openai import OpenAI
from together import Together

# Initialize the Together API client
#client = OpenAI()
client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

def main():
    st.title('SportsBot ⚽️🏀🏈🥎🎱')

    st.markdown("""
    <h1 style='color: white; font-size: 24px;'>NBA? NFL? I have got it covered, ask me anything about stats, games, or players!</h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <style>
    
        /* Increase font size of all text inputs */
        .stTextInput input {
            font-size: 26px; /* Change the font size of input text */
        }
        /* Increase font size of the label of text inputs */
        .stTextInput label {
            font-size: 30px; /* Change the font size of the label */
        }
        /* General font size increase for other elements if needed */
        html, body, .stText, .stButton, .stTextarea {
            font-size: 28px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Ensure session state for conversation is initialized properly
    if 'conversation' not in st.session_state:
        st.session_state['conversation'] = []
    
    # User input
    user_input = st.text_input("")
    
    if st.button("ASK"):
        if user_input:
            # Append user message to conversation
            st.session_state.conversation.append(f"You: {user_input}")
            # Generate and append AI response
            response = generate_response(user_input)
            st.session_state.conversation.append(f"Bot: {response}")

    # Display conversation
    for message in st.session_state.conversation:
        st.text(message)

def generate_response(user_input):
    response = client.chat.completions.create(
        model="meta-llama/Llama-3-8b-chat-hf",
        messages=[{"role": "user", "content": user_input}],
    )
    return response.choices[0].message.content
    # response = client.chat.completions.create(
    #     model="gpt-3.5-turbo-0125",
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant with sports analysis."},
    #         {"role": "user", "content": user_input}
    #     ]
    # )
    # return response.choices[0].message.content

if __name__ == "__main__":
    main()
