import sys
import typing
import gpu


def batch_for_shader(shader: 'gpu.types.GPUShader',
                     type: str,
                     content: dict,
                     indices=None):
    """Return a batch already configured and compatible with the shader. 

    :param shader: shader for which a compatible format will be computed.
    :param type: “‘POINTS’, ‘LINES’, ‘TRIS’ or ‘LINES_ADJ’”.
    :param content: Maps the name of the shader attribute with the data to
    fill the vertex buffer.
    :return:  compatible batch 
    """

    pass
