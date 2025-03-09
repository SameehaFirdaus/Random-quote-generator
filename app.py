import streamlit as st
import random

# List of motivational quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. - William James",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson"
]

# Streamlit app
st.title("Random Quote Generator")
st.write("Refresh the page to get a new motivational quote!")

# Select a random quote
random_quote = random.choice(quotes)

# Display the quote
st.subheader(random_quote)
