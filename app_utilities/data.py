import os 

style_name = ['Munch', 'Monet', 'Monet_2', 'Picasso','Van Gogh', 'Turner', 'Afremov', 'Space', 'Space_2', 'Escher']
style_file = ['munch.jpg','monet.jpg', 'monet2.jpg', 'picasso.jpg', 'vangogh.jpg','turner.jpg', 'afremov.jpg', 'space.jpg', 'pillars.jpg', 'escher.jpg']

style_path = 'style/'

style_dict = {name: os.path.join(style_path, filee) for name, filee in zip(style_name, style_file)}

content_name = ['Ballerina', 'Golden Gate','Mountains', 'Nature', 'Temple', 'Colosseum', 'NYC', 'Piramids', 'Great Wall of China']
content_file = ['dancing.jpg', 'golden_gate.jpg', 'mountains.jpg', 'nature.jpg', 'Kinkaku-ji.jpg', 'colosseum.jpg', 'nyc.jpg', 'piramids.jpg', 'great-wall.jpg']

content_path = 'content/'

content_images_dict = {name: os.path.join(content_path, filee) for name, filee in zip(content_name, content_file)}


