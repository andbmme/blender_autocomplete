# -*- coding: utf-8 -*-
from typing import List, Union

import bpy


def brush_edit(stroke: List['bpy.types.OperatorStrokeElement'] = None):
    """Apply a stroke of brush to the particles 

    :param stroke: Stroke 
    """

    pass


def connect_hair(all: bool = False):
    """Connect hair to the emitter mesh 

    :param all: All hair, Connect all hair systems to the emitter mesh 
    """

    pass


def copy_particle_systems(space: Union[str, int] = 'OBJECT',
                          remove_target_particles: bool = True,
                          use_active: bool = False):
    """Copy particle systems from the active object to selected objects 

    :param space: Space, Space transform for copying from one object to
    anotherOBJECT Object, Copy inside each object’s local space.WORLD World,
    Copy in world space.
    :param remove_target_particles: Remove Target Particles, Remove particle
    systems on the target objects
    :param use_active: Use Active, Use the active particle system from the
    context
    """

    pass


def delete(type: Union[str, int] = 'PARTICLE'):
    """Delete selected particles or keys 

    :param type: Type, Delete a full particle or only keys 
    """

    pass


def disconnect_hair(all: bool = False):
    """Disconnect hair from the emitter mesh 

    :param all: All hair, Disconnect all hair systems from the emitter mesh 
    """

    pass


def duplicate_particle_system(use_duplicate_settings: bool = False):
    """Duplicate particle system within the active object 

    :param use_duplicate_settings: Duplicate Settings, Duplicate settings as
    well, so the new particle system uses its own settings
    """

    pass


def dupliob_copy():
    """Duplicate the current dupliobject 

    """

    pass


def dupliob_move_down():
    """Move dupli object down in the list 

    """

    pass


def dupliob_move_up():
    """Move dupli object up in the list 

    """

    pass


def dupliob_refresh():
    """Refresh list of dupli objects and their weights 

    """

    pass


def dupliob_remove():
    """Remove the selected dupliobject 

    """

    pass


def edited_clear():
    """Undo all edition performed on the particle system 

    """

    pass


def hair_dynamics_preset_add(name: str = "",
                             remove_name: bool = False,
                             remove_active: bool = False):
    """Add or remove a Hair Dynamics Preset 

    :param name: Name, Name of the preset, used to make the path name 
    :param remove_name: remove_name
    :param remove_active: remove_active
    """

    pass


def hide(unselected: bool = False):
    """Hide selected particles 

    :param unselected: Unselected, Hide unselected rather than selected 
    """

    pass


def mirror():
    """Duplicate and mirror the selected particles along the local X axis 

    """

    pass


def new():
    """Add new particle settings 

    """

    pass


def new_target():
    """Add a new particle target 

    """

    pass


def particle_edit_toggle():
    """Toggle particle edit mode 

    """

    pass


def rekey(keys_number: int = 2):
    """Change the number of keys of selected particles (root and tip keys
    included)

    :param keys_number: Number of Keys 
    """

    pass


def remove_doubles(threshold: float = 0.0002):
    """Remove selected particles close enough of others 

    :param threshold: Merge Distance, Threshold distance within which
    particles are removed
    """

    pass


def reveal(select: bool = True):
    """Show hidden particles 

    :param select: Select 
    """

    pass


def select_all(action: Union[str, int] = 'TOGGLE'):
    """(De)select all particles’ keys 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle
    selection for all elements.SELECT Select, Select all elements.DESELECT
    Deselect, Deselect all elements.INVERT Invert, Invert selection of all
    elements.
    """

    pass


def select_less():
    """Deselect boundary selected keys of each particle 

    """

    pass


def select_linked(deselect: bool = False, location: int = (0, 0)):
    """Select nearest particle from mouse pointer 

    :param deselect: Deselect, Deselect linked keys rather than selecting them 
    :param location: Location
    """

    pass


def select_more():
    """Select keys linked to boundary selected keys of each particle 

    """

    pass


def select_random(percent: float = 50.0,
                  seed: int = 0,
                  action: Union[str, int] = 'SELECT',
                  type: Union[str, int] = 'HAIR'):
    """Select a randomly distributed set of hair or points 

    :param percent: Percent, Percentage of objects to select randomly 
    :param seed: Random Seed, Seed for the random number generator
    :param action: Action, Selection action to executeSELECT Select, Select
    all elements.DESELECT Deselect, Deselect all elements.
    :param type: Type, Select either hair or points
    """

    pass


def select_roots(action: Union[str, int] = 'SELECT'):
    """Select roots of all visible particles 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle
    selection for all elements.SELECT Select, Select all elements.DESELECT
    Deselect, Deselect all elements.INVERT Invert, Invert selection of all
    elements.
    """

    pass


def select_tips(action: Union[str, int] = 'SELECT'):
    """Select tips of all visible particles 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle
    selection for all elements.SELECT Select, Select all elements.DESELECT
    Deselect, Deselect all elements.INVERT Invert, Invert selection of all
    elements.
    """

    pass


def shape_cut():
    """Cut hair to conform to the set shape object 

    """

    pass


def subdivide():
    """Subdivide selected particles segments (adds keys) 

    """

    pass


def target_move_down():
    """Move particle target down in the list 

    """

    pass


def target_move_up():
    """Move particle target up in the list 

    """

    pass


def target_remove():
    """Remove the selected particle target 

    """

    pass


def unify_length():
    """Make selected hair the same length 

    """

    pass


def weight_set(factor: float = 1.0):
    """Set the weight of selected keys 

    :param factor: Factor, Interpolation factor between current brush weight,
    and keys’ weights
    """

    pass
