import bmesh


def intersect_face_point(face: 'bmesh.types.BMFace', point: float) -> bool:
    """ Tests if the projection of a point is inside a face (using the face’s
    normal).

    :param face: The face to test.
    :param point: The point to test.
    :return: Projection of the point is in the face.
    """

    pass
