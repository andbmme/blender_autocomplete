# -*- coding: utf-8 -*-
from typing import Union


def cycles_integrator_preset_add(name: str = "",
                                 remove_name: bool = False,
                                 remove_active: bool = False):
    """Add an Integrator Preset 

    :param name: Name, Name of the preset, used to make the path name 
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

    pass


def cycles_sampling_preset_add(name: str = "",
                               remove_name: bool = False,
                               remove_active: bool = False):
    """Add a Sampling Preset 

    :param name: Name, Name of the preset, used to make the path name 
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

    pass


def opengl(animation: bool = False,
           render_keyed_only: bool = False,
           sequencer: bool = False,
           write_still: bool = False,
           view_context: bool = True):
    """Take a snapshot of the active viewport 

    :param animation: Animation, Render files from the animation range of
    this scene
    :param render_keyed_only: Render Keyframes Only, Render only those frames
    where selected objects have a key in their animation data. Only used when
    rendering animation
    :param sequencer: Sequencer, Render using the sequencer’s OpenGL display
    :param write_still: Write Image, Save rendered the image to the output
    path (used only when animation is disabled)
    :param view_context: View Context, Use the current 3D view for rendering,
    else use scene settings
    """

    pass


def play_rendered_anim():
    """Play back rendered frames/movies using an external player 

    """

    pass


def preset_add(name: str = "",
               remove_name: bool = False,
               remove_active: bool = False):
    """Add or remove a Render Preset 

    :param name: Name, Name of the preset, used to make the path name 
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

    pass


def render(animation: bool = False,
           write_still: bool = False,
           use_viewport: bool = False,
           layer: str = "",
           scene: str = ""):
    """Render active scene 

    :param animation: Animation, Render files from the animation range of
    this scene
    :param write_still: Write Image, Save rendered the image to the output
    path (used only when animation is disabled)
    :param use_viewport: Use 3D Viewport, When inside a 3D viewport,
    use layers and camera of the viewport
    :param layer: Render Layer, Single render layer to re-render (used only
    when animation is disabled)
    :param scene: Scene, Scene to render, current scene if not specified
    """

    pass


def shutter_curve_preset(shape: Union[str, int] = 'SMOOTH'):
    """Set shutter curve 

    :param shape: Mode 
    """

    pass


def view_cancel():
    """Cancel show render view 

    """

    pass


def view_show():
    """Toggle show render view 

    """

    pass
