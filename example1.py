'''Streamlit example application demonstrating various UI components.'''
from PIL import Image
import streamlit as st

st.title("Hello GeeksForGeeks !!!")
st.header("This is a header!")
st.subheader("This is a subheader!")

st.markdown("### This is a markdown")

st.success("Success")

st.info("Information")

st.warning("Warning")

st.error("Error")

exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

st.write("Text with write")

# Writing python inbuilt function range()
st.write(range(10))
for r in range(10):
    st.write(r)

img = Image.open("streamlit.png") # Open the image file
st.image(img, width=200) # Display the image with a specified width

# Display a checkbox with the label 'Show/Hide'
if st.checkbox("Show/Hide"):
    # Show this text only when the checkbox is checked
    st.text("Showing the widget")
    
st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')