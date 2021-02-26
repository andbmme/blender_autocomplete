import sys
import typing
import bpy


def bake_action(obj: 'bpy.types.Object', *, action: 'bpy.types.Action',
                frames: int, **kwargs) -> 'bpy.types.Action':
    """

    :param obj: Object to bake.
    :param action: An action to bake the data into, or None for a new action
    to be created.
    :param frames: Frames to bake.
    :return: an action or None
    """

    pass


def bake_action_iter(obj: 'bpy.types.Object',
                     *,
                     action: 'bpy.types.Action',
                     only_selected: bool = False,
                     do_pose: bool = True,
                     do_object: bool = True,
                     do_visual_keying: bool = True,
                     do_constraint_clear: bool = False,
                     do_parents_clear: bool = False,
                     do_clean: bool = False) -> 'bpy.types.Action':
    """An coroutine that bakes action for a single object. 

    :param obj: Object to bake.
    :param action: An action to bake the data into, or None for a new action
    to be created.
    :param only_selected: Only bake selected bones.
    :param do_pose: Bake pose channels.
    :param do_object: Bake objects.
    :param do_visual_keying: Use the final transformations for baking (
    ‘visual keying’)
    :param do_constraint_clear: Remove constraints after baking.
    :param do_parents_clear: Unparent after baking objects.
    :param do_clean: Remove redundant keyframes after baking.
    :return:  an action or None 
    """

    pass


def bake_action_objects(object_action_pairs, *, frames: int,
                        **kwargs) -> typing.List['bpy.types.Action']:
    """A version of bake_action_objects_iter() that takes frames and returns
    the output.

    :param frames: Frames to bake.
    :return:  A sequence of Action (aligned with
    object_action_pairs)
    """

    pass


def bake_action_objects_iter(object_action_pairs: 'bpy.types.Object',
                             **kwargs):
    """An coroutine that bakes actions for multiple objects. 

    :param object_action_pairs: Sequence of object action tuples, action is
    the destination for the baked data. When None a new action will be created.
    """

    pass
