import sys
import typing
import bpy
import mathutils


class AddObjectHelper:
    def align_update_callback(self, _context):
        """

        """
        pass


def add_object_align_init(
        context: 'bpy.types.Context',
        operator: 'bpy.types.Operator') -> 'mathutils.Matrix':
    """Return a matrix using the operator settings and view context. 

    :param context: The context to use.
    :param operator: The operator, checked for location and rotation
    properties.
    :return:  the matrix from the context and settings. 
    """

    pass


def object_add_grid_scale(context):
    """Return scale which should be applied on object data to align it to
    grid scale

    """

    pass


def object_add_grid_scale_apply_operator(operator, context):
    """Scale an operators distance values by the grid size. 

    """

    pass


def object_data_add(context: 'bpy.types.Context',
                    obdata: 'bpy.data',
                    operator: 'bpy.types.Operator' = None,
                    name: str = "") -> 'bpy.types.Object':
    """Add an object using the view context and preference to initialize the
    location, rotation and layer.

    :param context: The context to use.
    :param obdata: the data used for the new object.
    :param operator: The operator, checked for location and rotation
    properties.
    :param name: Optional name
    :return:  the newly created object in the scene. 
    """

    pass


def world_to_camera_view(scene: 'bpy.types.Scene', obj: 'bpy.types.Object',
                         coord: 'mathutils.Vector') -> 'mathutils.Vector':
    """Takes shift-x/y, lens angle and sensor size into account as well as
    perspective/ortho projections.

    :param scene: Scene to use for frame size.
    :param obj: Camera object.
    :param coord: World space location.
    :return:  a vector where X and Y map to the view plane and Z is the depth
    on the view axis.
    """

    pass
