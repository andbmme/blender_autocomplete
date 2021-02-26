import sys
import typing
import mathutils


def draw_circle_2d(position: 'mathutils.Vector',
                   color,
                   radius: float,
                   segments: int = 32):
    """Draw a circle. 

    :param position: Position where the circle will be drawn.
    :param color: Color of the circle. To use transparency GL_BLEND has to be
    enabled.
    :param radius: Radius of the circle.
    :param segments: How many segments will be used to draw the circle.
    Higher values give besser results but the drawing will take longer.
    """

    pass


def draw_texture_2d(texture_id: int, position: 'mathutils.Vector',
                    width: float, height: float):
    """Draw a 2d texture. 

    :param texture_id: OpenGL id of the texture (e.g.
    bpy.types.Image.bindcode).
    :param position: Position of the lower left corner.
    :param width: Width of the image when drawn (not necessarily the original
    width of the texture).
    :param height: Height of the image when drawn.
    """

    pass
