import streamlit as st
import openai
import nltk
from textblob import TextBlob
from langdetect import detect, DetectorFactory
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Initialize OpenAI API key
openai.api_key = 'https://api.openai.com/v1/chat/completions'

# Set the title of the app
st.title("AI-Powered Blog Generation System")

# 1. **Style Customization**
st.sidebar.header("Style Customization")
style = st.sidebar.selectbox("Choose Style", ["Professional", "Casual", "Technical", "Creative"])

# 2. **Terminology Integration**
terms = st.sidebar.text_input("Add Specific Terminology (comma-separated)", "")


# 3. **Content Structure**
st.sidebar.header("Content Structure")
structure = st.sidebar.selectbox("Choose Content Structure", ["Introduction, Body, Conclusion", "Q&A", "Listicles", "How-To"])

# 4. **SEO Optimization**
st.sidebar.header("SEO Optimization")
keywords = st.sidebar.text_input("Add SEO Keywords (comma-separated)", "")

# 5. **Tone and Sentiment Analysis**
st.sidebar.header("Tone and Sentiment Analysis")
sentiment_check = st.sidebar.checkbox("Enable Sentiment Analysis")

# 6. **Sources and Fact-Checking**
st.sidebar.header("Sources and Fact-Checking")
sources = st.sidebar.text_area("Add Source Links (comma-separated)", "")

# 7. **Customizable Output Formats**
st.sidebar.header("Customizable Output Formats")
format_choice = st.sidebar.selectbox("Choose Output Format", ["Plain Text", "Markdown", "HTML"])

# 8. **Performance Analytics**
st.sidebar.header("Performance Analytics")
analysis_enable = st.sidebar.checkbox("Enable Performance Analytics")

# 9. **Multilingual Support**
st.sidebar.header("Multilingual Support")
language = st.sidebar.selectbox("Choose Language", ["English", "Spanish", "French", "German"])

# Content Generation
st.header("Generate Your Blog")
prompt = st.text_area("Enter the blog topic or prompt here")

if st.button("Generate Blog"):
    # Create the prompt for the AI
    ai_prompt = f"Generate a {style} blog post about {prompt} with the following structure: {structure}. Include terms: {terms}. Optimize for keywords: {keywords}."

    # Request to OpenAI GPT
    response = openai.chat.completions.create(
        model="davinci-codex",  # Change to your preferred engine
        messages=ai_prompt,
        stream=True
    )
    blog_content = response.choices[0].text.strip()

    # 5. **Tone and Sentiment Analysis**
    if sentiment_check:
        blob = TextBlob(blog_content)
        sentiment = blob.sentiment.polarity
        st.write(f"Sentiment Score: {sentiment}")

    # Translate content if needed
    if language != "English":
        detected_language = detect(blog_content)
        st.write(f"Detected Language: {detected_language}")

        # Simple translation (replace this with a real translation API call)
        st.write(f"Translated Content (Simulated): {blog_content}")

    # Display the blog content
    st.subheader("Generated Blog Content")
    if format_choice == "Plain Text":
        st.write(blog_content)
    elif format_choice == "Markdown":
        st.markdown(blog_content)
    elif format_choice == "HTML":
        st.markdown(blog_content, unsafe_allow_html=True)

    # 8. **Performance Analytics**
    if analysis_enable:
        # Example analytics (replace with real analytics if needed)
        st.write("Performance Analytics (Simulated):")
        data = {
            'Metric': ['Word Count', 'Sentiment Score'],
            'Value': [len(blog_content.split()), sentiment]
        }
        df = pd.DataFrame(data)
        st.write(df)

        # Plot example (simple word count)
        plt.figure(figsize=(10, 4))
        sns.barplot(x='Metric', y='Value', data=df)
        st.pyplot(plt)

# 6. **Sources and Fact-Checking**
if sources:
    st.subheader("Sources")
    st.write(sources)

# 7. **Customizable Output Formats**
st.sidebar.text("Output Format selected: " + format_choice)

# 9. **Multilingual Support**
st.sidebar.text("Language selected: " + language)
