"""
Style Transfer
"""

import os
import base64

def transfer(input_image_name, style, color):
    """
    Load model and perform style transfer on input image
    :param input_image_name: filename of an input image
    :param style: a style name before '-' in image filename
    :return: output_image
    """

    output_image = '../images/output/' + style + '-' + input_image_name.rstrip('.jpg')
    if color == "True":
        output_image += '-color'
    output_image += '.jpg'
    encoded__output_image = base64.b64encode(open(output_image, 'rb').read())

    return encoded__output_image