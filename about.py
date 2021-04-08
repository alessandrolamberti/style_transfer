import streamlit as st 
'''
File for about section
'''

def about():
    st.markdown("""
    ## What neural style transfer is about?

    We know art has been around since thousands of years. Just recently we started asking if artists, paintings leave a sort of "fingerprint".

    Neural Style Transfer (NST), as seen, merges two images: a "content" image and a "style" image, to create a synthetic new image, 
    which combines the content of the former, with the styilistic features of the latter. 

    ### Original work

    The original algorithm is by [Gatys et al. (2015).](https://arxiv.org/abs/1508.06576). It's about the implementation of a well-known Neural 
    Network, the VGG-19, a Convolutional Neural Network, where each layer of units can be understood as a collection of image filters, each of which
    extracts a certain feature from the input image. Thus, the output of a given layer consists of
    so-called feature maps: differently filtered versions of the input image.
    
    When Convolutional Neural Networks are trained on object recognition, they develop a
    representation of the image that makes object information increasingly explicit along the processing hierarchy. Therefore, along the processing hierarchy of the network, the input image
    is transformed into representations that increasingly care about the actual content of the image compared to its detailed pixel values (that's why it's important, during the training,
    to accurately choose the layers from which extract the image features, usually the middle-late ones). 
    
    We can directly visualise the information each layer
    contains about the input image by reconstructing the image only from the feature maps in that layer.""")

    st.image('images/architecture.png', width = 750)


    st.markdown("""
    The content image and the style image are fed through the CNN, and network activations are sampled at a late convolution layer of the VGG-19 architecture.
    For the style image, those activations are then stored in a [Gramian matrix](https://en.wikipedia.org/wiki/Gramian_matrix).
    
    Once done, the algorithm is based on three major steps:
    - Build the content cost function $J_{content}(C,G)$
    - Build the style cost function $J_{style}(S,G)$
    - Put it together to get $J(G) = a J_{content}(C,G) + b J_{style}(S,G)$, the object to minimize.

    However, this is proven to be a slow optimization algorithm, although it works on any arbitrary image.

    Subsequent work developed a method for fast artistic style transfer that may operate in real time, 
    but was limited to one or a limited set of styles.

    ### Faster optimization algorithm

    [Golnaz Ghiasi et al. (2017)](https://arxiv.org/abs/1705.06830) Proposed a new implementation of the original work, which combines the flexibility of the neural algorithm of artistic 
    style with the speed of fast style transfer networks to allow real-time stylization using any content/style image pair. This algorithm permits style interpolation in real-time, even when done on video media.

    This work proposes to build a style transfer network as a typical encoder/decoder
    architecture but specialize the normalization parameters specific to each painting style, and a style prediction network.""")

    st.image('images/architecture2.png')

    st.markdown("""

    Those 2 networks are then trained on the Imagenet database, and the Describable Textures Dataset used as the corpus of training style images, for a total of 80000+ images.

    The model was found able to generalize to any content/tyle image pair.
    
    """)
