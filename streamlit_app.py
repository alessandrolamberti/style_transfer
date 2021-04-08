from utils import transfer, load_image, load_model, show_images, download
from data import *
import streamlit as st 

st.set_page_config(page_title='Style Transfer', layout= 'wide', page_icon= "images/icon.png")
st.title('Style Transfer App')
st.sidebar.title('Navigation')
page = st.sidebar.selectbox("Select page:", options = ["Welcome", "App", "About"])

if page == 'Welcome':
    st.header("Welcome to the Neural Style Transfer App!")
    st.markdown('By <a href="https://www.linkedin.com/in/alessandro-lamberti/" target="_blank">Alessandro Lamberti</a>' , unsafe_allow_html=True)
    st.markdown("### Please select the page you want to navigate to.")
    st.markdown("""
    - App: try the app, you can choose your own images for both style and content, or try the pre-loaded ones.

            - Style: typically a painting you like.
            - Content: any image you'd like the painting's style applied to.
                """)
    st.markdown("- About: to read more about the neural network and the algorithm behind the hooks, see what style transfer is about.")
    st.image('images/example.png', width= 1100)

elif page == 'App':
    option = st.sidebar.radio('What do you prefer?', options = ['Custom images', 'Pre-loaded images'])

    if option == 'Custom images':
        content = st.sidebar.file_uploader("Choose a content image", type=['png', 'jpg', 'jpeg', 'jfif'])
        

    else:
        content_name = st.sidebar.selectbox("Choose the content images:", content_name)
        content = content_images_dict[content_name]

    style_option = st.sidebar.radio('What about the style?', options = ['Custom style', 'Pre-loaded style'])

    if style_option == 'Custom style':
        style = st.sidebar.file_uploader("Choose a style image", type=['png', 'jpg', 'jpeg'])
        
            
    else:
        style_name = st.sidebar.selectbox("Choose a style:", style_name)
        style= style_dict[style_name]

    if content and style != None:
        content_image = load_image(content)
        style_image = load_image(style)


        model = load_model()
        stylized = transfer(model, content_image, style_image)
        show_images([content_image, style_image, stylized], titles = ['Original content image', 'Style image', 'Stylized image'])
        st.write('If you want, you can download your new image')
        st.markdown(download([content_image, style_image, stylized]), unsafe_allow_html=True)
    else:
        st.warning("Please upload a style/content image or change option.")

else:
    st.header("About section")
    st.markdown("""
    Coming soon!
    """)













    