import streamlit as st

# Title and introductory message
st.title(" My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/). Here are some basic UI elements to get you going:"
)

# Interactive elements
st.subheader("Let's get interactive:")

# Text input with placeholder
name = st.text_input("Enter your name:", placeholder="Your Name")

# Conditional greeting based on input
if name:
    st.write(f"Hi {name}! Welcome to my app.")
else:
    st.write("Please enter your name to see a personalized greeting.")

# Slider for temperature selection
temperature = st.slider("Choose a temperature:", min_value=0, max_value=100, step=1)
st.write(f"Selected temperature: {temperature}°C")

# Select box for choosing a color
color_options = ["Red", "Green", "Blue", "Yellow"]
selected_color = st.selectbox("Pick a color:", color_options)
st.write(f"You selected: {selected_color}")

# Checkbox for user preference
preference = st.checkbox("Do you like Streamlit?")
if preference:
    st.write("Great! We're glad you enjoy it.")
else:
    st.write("We're always working to improve. Tell us how we can make Streamlit better for you!")

# Image display for visual appeal
st.image("https://placeimg.com/640/480/animals", caption="A friendly animal")

# Expandable section with additional information

st.expander("Want to learn more about Streamlit?"):
    st.write(
        "Streamlit simplifies the creation of data apps. Visit the documentation to explore more components and build richer experiences!"
    )