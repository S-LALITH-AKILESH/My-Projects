import streamlit as st
from PIL import Image

st.set_page_config(page_title="Miniprjt", page_icon=":tada:", layout="wide")

st.title("INDIAN ELECTION SENTIMENTAL ANALYSIS - 2024")
st.write("##")
st.write("Welcome User, this miniproject helps in performing the sentimental analysis over updated tweets regarding our National Leaders: **NARENDRA DAMODARDAS MODI** and **RAHUL RAJIV GANDHI**")
st.write("##")

image = Image.open(r"C:\Users\ASUS\Desktop\Jupyter\miniprjt\pictures\modi.jpg")

#st.image(image, caption='MODI')

image1 = Image.open(r"C:\Users\ASUS\Desktop\Jupyter\miniprjt\pictures\rahul.jpg")

#st.image(image1, caption='RAHUL')

images = [image, image1]
#st.image(images, width=300, caption=["some generic text"] * len(images))

# List of captions for each image
captions = ["MODI", "RAHUL"]

# Define the width and height for each image
image_width = 500

# Display images and captions side by side with a little space in between

col1, col2 = st.columns(2)
with col1:
    st.image(images[0], use_column_width=False, width=image_width, caption=captions[0])

with col2:
    st.image(images[1], use_column_width=False, width=image_width, caption=captions[1])

st.write("##")

from textblob import TextBlob

def find_polarity(review):
    return TextBlob(review).sentiment.polarity

st.title("COMMENT BOX:")

sentence = st.text_input('Write your comment below:') 

if sentence:
    x = find_polarity(sentence)
    if x >= 0:
        st.write("Positive Comment.")
    else:
        st.write("Negative Comment.")
    

st.write("##")

st.write("To run the project please click the 'PREDICTION' button.")

result = st.button("PREDICTION")

if result:

    import streamlit as st
    import pickle

    # Display the Plotly figure saved as HTML
    st.markdown("<h1>Sentimental Analysis based on Tweets</h1>", unsafe_allow_html=True)
    st.components.v1.html(open('plotly_figure.html', 'r', encoding='utf-8').read(), height=600)

    # Load your saved image from Matplotlib
    image = Image.open('matplotlib_figure.png')

    # Display the image in Streamlit
    st.image(image, caption='Matplotlib Plot', use_column_width=True)


    with open('file.pk1', 'rb') as file:

        myvar = pickle.load(file)

        st.write(myvar)


    