import sys
import typing
import bpy


def change_effect_input(swap: typing.Union[int, str] = 'A_B'):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param swap: Swap, The effect inputs to swap 
    :type swap: typing.Union[int, str]
    '''

    pass


def change_effect_type(type: typing.Union[int, str] = 'CROSS'):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param type: Type, Sequencer effect typeCROSS Crossfade, Crossfade effect strip type.ADD Add, Add effect strip type.SUBTRACT Subtract, Subtract effect strip type.ALPHA_OVER Alpha Over, Alpha Over effect strip type.ALPHA_UNDER Alpha Under, Alpha Under effect strip type.GAMMA_CROSS Gamma Cross, Gamma Cross effect strip type.MULTIPLY Multiply, Multiply effect strip type.OVER_DROP Alpha Over Drop, Alpha Over Drop effect strip type.WIPE Wipe, Wipe effect strip type.GLOW Glow, Glow effect strip type.TRANSFORM Transform, Transform effect strip type.COLOR Color, Color effect strip type.SPEED Speed, Color effect strip type.MULTICAM Multicam Selector.ADJUSTMENT Adjustment Layer.GAUSSIAN_BLUR Gaussian Blur.TEXT Text.COLORMIX Color Mix. 
    :type type: typing.Union[int, str]
    '''

    pass


def change_path(filepath: str = "",
                directory: str = "",
                files: typing.List['bpy.types.OperatorFileListElement'] = None,
                hide_props_region: bool = True,
                filter_blender: bool = False,
                filter_backup: bool = False,
                filter_image: bool = False,
                filter_movie: bool = False,
                filter_python: bool = False,
                filter_font: bool = False,
                filter_sound: bool = False,
                filter_text: bool = False,
                filter_archive: bool = False,
                filter_btx: bool = False,
                filter_collada: bool = False,
                filter_alembic: bool = False,
                filter_folder: bool = True,
                filter_blenlib: bool = False,
                filemode: int = 9,
                relative_path: bool = True,
                display_type: typing.Union[int, str] = 'DEFAULT',
                sort_method: typing.Union[int, str] = 'FILE_SORT_ALPHA',
                use_placeholders: bool = False):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param filepath: File Path, Path to file 
    :type filepath: str
    :param directory: Directory, Directory of the file 
    :type directory: str
    :param files: Files 
    :type files: typing.List['bpy.types.OperatorFileListElement']
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings 
    :type hide_props_region: bool
    :param filter_blender: Filter .blend files 
    :type filter_blender: bool
    :param filter_backup: Filter .blend files 
    :type filter_backup: bool
    :param filter_image: Filter image files 
    :type filter_image: bool
    :param filter_movie: Filter movie files 
    :type filter_movie: bool
    :param filter_python: Filter python files 
    :type filter_python: bool
    :param filter_font: Filter font files 
    :type filter_font: bool
    :param filter_sound: Filter sound files 
    :type filter_sound: bool
    :param filter_text: Filter text files 
    :type filter_text: bool
    :param filter_archive: Filter archive files 
    :type filter_archive: bool
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file 
    :type relative_path: bool
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_VERTICAL Short List, Display files as short list.LIST_HORIZONTAL Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting modeFILE_SORT_ALPHA Name, Sort the file list alphabetically.FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.FILE_SORT_TIME Modified Date, Sort files by modification time.FILE_SORT_SIZE Size, Sort files by size. 
    :type sort_method: typing.Union[int, str]
    :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip 
    :type use_placeholders: bool
    '''

    pass


def copy():
    '''Copy selected strips to clipboard 

    '''

    pass


def crossfade_sounds():
    '''Do cross-fading volume animation of two selected sound strips 

    '''

    pass


def cut(frame: int = 0,
        type: typing.Union[int, str] = 'SOFT',
        side: typing.Union[int, str] = 'MOUSE'):
    '''Cut the selected strips 

    :param frame: Frame, Frame where selected strips will be cut 
    :type frame: int
    :param type: Type, The type of cut operation to perform on strips 
    :type type: typing.Union[int, str]
    :param side: Side, The side that remains selected after cutting 
    :type side: typing.Union[int, str]
    '''

    pass


def cut_multicam(camera: int = 1):
    '''Cut multi-cam strip and select camera 

    :param camera: Camera 
    :type camera: int
    '''

    pass


def deinterlace_selected_movies():
    '''Deinterlace all selected movie sources 

    '''

    pass


def delete():
    '''Erase selected strips from the sequencer 

    '''

    pass


def duplicate(mode: typing.Union[int, str] = 'TRANSLATION'):
    '''Duplicate the selected strips 

    :param mode: Mode 
    :type mode: typing.Union[int, str]
    '''

    pass


def duplicate_move(SEQUENCER_OT_duplicate=None, TRANSFORM_OT_seq_slide=None):
    '''Duplicate selected strips and move them 

    :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips 
    :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time 
    '''

    pass


def effect_strip_add(frame_start: int = 0,
                     frame_end: int = 0,
                     channel: int = 1,
                     replace_sel: bool = True,
                     overlap: bool = False,
                     type: typing.Union[int, str] = 'CROSS',
                     color: float = (0.0, 0.0, 0.0)):
    '''Add an effect to the sequencer, most are applied on top of existing strips 

    :param frame_start: Start Frame, Start frame of the sequence strip 
    :type frame_start: int
    :param frame_end: End Frame, End frame for the color strip 
    :type frame_end: int
    :param channel: Channel, Channel to place this strip into 
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection 
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don’t correct overlap on new sequence strips 
    :type overlap: bool
    :param type: Type, Sequencer effect typeCROSS Crossfade, Crossfade effect strip type.ADD Add, Add effect strip type.SUBTRACT Subtract, Subtract effect strip type.ALPHA_OVER Alpha Over, Alpha Over effect strip type.ALPHA_UNDER Alpha Under, Alpha Under effect strip type.GAMMA_CROSS Gamma Cross, Gamma Cross effect strip type.MULTIPLY Multiply, Multiply effect strip type.OVER_DROP Alpha Over Drop, Alpha Over Drop effect strip type.WIPE Wipe, Wipe effect strip type.GLOW Glow, Glow effect strip type.TRANSFORM Transform, Transform effect strip type.COLOR Color, Color effect strip type.SPEED Speed, Color effect strip type.MULTICAM Multicam Selector.ADJUSTMENT Adjustment Layer.GAUSSIAN_BLUR Gaussian Blur.TEXT Text.COLORMIX Color Mix. 
    :type type: typing.Union[int, str]
    :param color: Color, Initialize the strip with this color (only used when type=’COLOR’) 
    :type color: float
    '''

    pass


def enable_proxies(proxy_25: bool = False,
                   proxy_50: bool = False,
                   proxy_75: bool = False,
                   proxy_100: bool = False,
                   overwrite: bool = False):
    '''Enable selected proxies on all selected Movie, Image and Meta strips 

    :param proxy_25: 25% 
    :type proxy_25: bool
    :param proxy_50: 50% 
    :type proxy_50: bool
    :param proxy_75: 75% 
    :type proxy_75: bool
    :param proxy_100: 100% 
    :type proxy_100: bool
    :param overwrite: Overwrite 
    :type overwrite: bool
    '''

    pass


def export_subtitles(filepath: str = "",
                     hide_props_region: bool = True,
                     check_existing: bool = True,
                     filter_blender: bool = False,
                     filter_backup: bool = False,
                     filter_image: bool = False,
                     filter_movie: bool = False,
                     filter_python: bool = False,
                     filter_font: bool = False,
                     filter_sound: bool = False,
                     filter_text: bool = False,
                     filter_archive: bool = False,
                     filter_btx: bool = False,
                     filter_collada: bool = False,
                     filter_alembic: bool = False,
                     filter_folder: bool = True,
                     filter_blenlib: bool = False,
                     filemode: int = 8,
                     display_type: typing.Union[int, str] = 'DEFAULT',
                     sort_method: typing.Union[int, str] = 'FILE_SORT_ALPHA'):
    '''Export .srt file containing text strips 

    :param filepath: File Path, Path to file 
    :type filepath: str
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings 
    :type hide_props_region: bool
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: bool
    :param filter_blender: Filter .blend files 
    :type filter_blender: bool
    :param filter_backup: Filter .blend files 
    :type filter_backup: bool
    :param filter_image: Filter image files 
    :type filter_image: bool
    :param filter_movie: Filter movie files 
    :type filter_movie: bool
    :param filter_python: Filter python files 
    :type filter_python: bool
    :param filter_font: Filter font files 
    :type filter_font: bool
    :param filter_sound: Filter sound files 
    :type filter_sound: bool
    :param filter_text: Filter text files 
    :type filter_text: bool
    :param filter_archive: Filter archive files 
    :type filter_archive: bool
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_VERTICAL Short List, Display files as short list.LIST_HORIZONTAL Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting modeFILE_SORT_ALPHA Name, Sort the file list alphabetically.FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.FILE_SORT_TIME Modified Date, Sort files by modification time.FILE_SORT_SIZE Size, Sort files by size. 
    :type sort_method: typing.Union[int, str]
    '''

    pass


def fades_add(duration_seconds: float = 1.0,
              type: typing.Union[int, str] = 'IN_OUT'):
    '''Adds or updates a fade animation for either visual or audio strips 

    :param duration_seconds: Fade Duration, Duration of the fade in seconds 
    :type duration_seconds: float
    :param type: Fade type, Fade in, out, both in and out, to, or from the playhead. Default is both in and outIN_OUT Fade In And Out, Fade selected strips in and out.IN Fade In, Fade in selected strips.OUT Fade Out, Fade out selected strips.CURSOR_FROM From Playhead, Fade from the time cursor to the end of overlapping sequences.CURSOR_TO To Playhead, Fade from the start of sequences under the time cursor to the current frame. 
    :type type: typing.Union[int, str]
    '''

    pass


def fades_clear():
    '''Removes fade animation from selected sequences 

    '''

    pass


def gap_insert(frames: int = 10):
    '''Insert gap at current frame to first strips at the right, independent of selection or locked state of strips 

    :param frames: Frames, Frames to insert after current strip 
    :type frames: int
    '''

    pass


def gap_remove(all: bool = False):
    '''Remove gap at current frame to first strip at the right, independent of selection or locked state of strips 

    :param all: All Gaps, Do all gaps to right of current frame 
    :type all: bool
    '''

    pass


def image_strip_add(
        directory: str = "",
        files: typing.List['bpy.types.OperatorFileListElement'] = None,
        hide_props_region: bool = True,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = True,
        filter_movie: bool = False,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = False,
        filter_text: bool = False,
        filter_archive: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 9,
        relative_path: bool = True,
        show_multiview: bool = False,
        use_multiview: bool = False,
        display_type: typing.Union[int, str] = 'DEFAULT',
        sort_method: typing.Union[int, str] = 'FILE_SORT_ALPHA',
        frame_start: int = 0,
        frame_end: int = 0,
        channel: int = 1,
        replace_sel: bool = True,
        overlap: bool = False,
        use_placeholders: bool = False):
    '''Add an image or image sequence to the sequencer 

    :param directory: Directory, Directory of the file 
    :type directory: str
    :param files: Files 
    :type files: typing.List['bpy.types.OperatorFileListElement']
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings 
    :type hide_props_region: bool
    :param filter_blender: Filter .blend files 
    :type filter_blender: bool
    :param filter_backup: Filter .blend files 
    :type filter_backup: bool
    :param filter_image: Filter image files 
    :type filter_image: bool
    :param filter_movie: Filter movie files 
    :type filter_movie: bool
    :param filter_python: Filter python files 
    :type filter_python: bool
    :param filter_font: Filter font files 
    :type filter_font: bool
    :param filter_sound: Filter sound files 
    :type filter_sound: bool
    :param filter_text: Filter text files 
    :type filter_text: bool
    :param filter_archive: Filter archive files 
    :type filter_archive: bool
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file 
    :type relative_path: bool
    :param show_multiview: Enable Multi-View 
    :type show_multiview: bool
    :param use_multiview: Use Multi-View 
    :type use_multiview: bool
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_VERTICAL Short List, Display files as short list.LIST_HORIZONTAL Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting modeFILE_SORT_ALPHA Name, Sort the file list alphabetically.FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.FILE_SORT_TIME Modified Date, Sort files by modification time.FILE_SORT_SIZE Size, Sort files by size. 
    :type sort_method: typing.Union[int, str]
    :param frame_start: Start Frame, Start frame of the sequence strip 
    :type frame_start: int
    :param frame_end: End Frame, End frame for the color strip 
    :type frame_end: int
    :param channel: Channel, Channel to place this strip into 
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection 
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don’t correct overlap on new sequence strips 
    :type overlap: bool
    :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip 
    :type use_placeholders: bool
    '''

    pass


def images_separate(length: int = 1):
    '''On image sequence strips, it returns a strip for each image 

    :param length: Length, Length of each frame 
    :type length: int
    '''

    pass


def lock():
    '''Lock strips so they can’t be transformed 

    '''

    pass


def mask_strip_add(frame_start: int = 0,
                   channel: int = 1,
                   replace_sel: bool = True,
                   overlap: bool = False,
                   mask: typing.Union[int, str] = ''):
    '''Add a mask strip to the sequencer 

    :param frame_start: Start Frame, Start frame of the sequence strip 
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into 
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection 
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don’t correct overlap on new sequence strips 
    :type overlap: bool
    :param mask: Mask 
    :type mask: typing.Union[int, str]
    '''

    pass


def meta_make():
    '''Group selected strips into a metastrip 

    '''

    pass


def meta_separate():
    '''Put the contents of a metastrip back in the sequencer 

    '''

    pass


def meta_toggle():
    '''Toggle a metastrip (to edit enclosed strips) 

    '''

    pass


def movie_strip_add(
        filepath: str = "",
        files: typing.List['bpy.types.OperatorFileListElement'] = None,
        hide_props_region: bool = True,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = False,
        filter_movie: bool = True,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = False,
        filter_text: bool = False,
        filter_archive: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 9,
        relative_path: bool = True,
        show_multiview: bool = False,
        use_multiview: bool = False,
        display_type: typing.Union[int, str] = 'DEFAULT',
        sort_method: typing.Union[int, str] = 'FILE_SORT_ALPHA',
        frame_start: int = 0,
        channel: int = 1,
        replace_sel: bool = True,
        overlap: bool = False,
        sound: bool = True,
        use_framerate: bool = True):
    '''Add a movie strip to the sequencer 

    :param filepath: File Path, Path to file 
    :type filepath: str
    :param files: Files 
    :type files: typing.List['bpy.types.OperatorFileListElement']
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings 
    :type hide_props_region: bool
    :param filter_blender: Filter .blend files 
    :type filter_blender: bool
    :param filter_backup: Filter .blend files 
    :type filter_backup: bool
    :param filter_image: Filter image files 
    :type filter_image: bool
    :param filter_movie: Filter movie files 
    :type filter_movie: bool
    :param filter_python: Filter python files 
    :type filter_python: bool
    :param filter_font: Filter font files 
    :type filter_font: bool
    :param filter_sound: Filter sound files 
    :type filter_sound: bool
    :param filter_text: Filter text files 
    :type filter_text: bool
    :param filter_archive: Filter archive files 
    :type filter_archive: bool
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file 
    :type relative_path: bool
    :param show_multiview: Enable Multi-View 
    :type show_multiview: bool
    :param use_multiview: Use Multi-View 
    :type use_multiview: bool
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_VERTICAL Short List, Display files as short list.LIST_HORIZONTAL Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting modeFILE_SORT_ALPHA Name, Sort the file list alphabetically.FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.FILE_SORT_TIME Modified Date, Sort files by modification time.FILE_SORT_SIZE Size, Sort files by size. 
    :type sort_method: typing.Union[int, str]
    :param frame_start: Start Frame, Start frame of the sequence strip 
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into 
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection 
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don’t correct overlap on new sequence strips 
    :type overlap: bool
    :param sound: Sound, Load sound with the movie 
    :type sound: bool
    :param use_framerate: Use Movie Framerate, Use framerate from the movie to keep sound and video in sync 
    :type use_framerate: bool
    '''

    pass


def movieclip_strip_add(frame_start: int = 0,
                        channel: int = 1,
                        replace_sel: bool = True,
                        overlap: bool = False,
                        clip: typing.Union[int, str] = ''):
    '''Add a movieclip strip to the sequencer 

    :param frame_start: Start Frame, Start frame of the sequence strip 
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into 
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection 
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don’t correct overlap on new sequence strips 
    :type overlap: bool
    :param clip: Clip 
    :type clip: typing.Union[int, str]
    '''

    pass


def mute(unselected: bool = False):
    '''Mute (un)selected strips 

    :param unselected: Unselected, Mute unselected rather than selected strips 
    :type unselected: bool
    '''

    pass


def offset_clear():
    '''Clear strip offsets from the start and end frames 

    '''

    pass


def paste():
    '''Paste strips from clipboard 

    '''

    pass


def reassign_inputs():
    '''Reassign the inputs for the effect strip 

    '''

    pass


def rebuild_proxy():
    '''Rebuild all selected proxies and timecode indices using the job system 

    '''

    pass


def refresh_all():
    '''Refresh the sequencer editor 

    '''

    pass


def reload(adjust_length: bool = False):
    '''Reload strips in the sequencer 

    :param adjust_length: Adjust Length, Adjust length of strips to their data length 
    :type adjust_length: bool
    '''

    pass


def rendersize():
    '''Set render size and aspect from active sequence 

    '''

    pass


def sample():
    '''Use mouse to sample color in current frame 

    '''

    pass


def scene_strip_add(frame_start: int = 0,
                    channel: int = 1,
                    replace_sel: bool = True,
                    overlap: bool = False,
                    scene: typing.Union[int, str] = ''):
    '''Add a strip to the sequencer using a blender scene as a source 

    :param frame_start: Start Frame, Start frame of the sequence strip 
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into 
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection 
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don’t correct overlap on new sequence strips 
    :type overlap: bool
    :param scene: Scene 
    :type scene: typing.Union[int, str]
    '''

    pass


def select(wait_to_deselect_others: bool = False,
           mouse_x: int = 0,
           mouse_y: int = 0,
           extend: bool = False,
           deselect_all: bool = False,
           linked_handle: bool = False,
           left_right: typing.Union[int, str] = 'NONE',
           linked_time: bool = False):
    '''Select a strip (last selected becomes the “active strip”) 

    :param wait_to_deselect_others: Wait to Deselect Others 
    :type wait_to_deselect_others: bool
    :param mouse_x: Mouse X 
    :type mouse_x: int
    :param mouse_y: Mouse Y 
    :type mouse_y: int
    :param extend: Extend, Extend the selection 
    :type extend: bool
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor 
    :type deselect_all: bool
    :param linked_handle: Linked Handle, Select handles next to the active strip 
    :type linked_handle: bool
    :param left_right: Left/Right, Select based on the current frame side the cursor is onNONE None, Don’t do left-right selection.MOUSE Mouse, Use mouse position for selection.LEFT Left, Select left.RIGHT Right, Select right. 
    :type left_right: typing.Union[int, str]
    :param linked_time: Linked Time, Select other strips at the same time 
    :type linked_time: bool
    '''

    pass


def select_active_side(side: typing.Union[int, str] = 'BOTH'):
    '''Select strips on the nominated side of the active strip 

    :param side: Side, The side of the handle that is selected 
    :type side: typing.Union[int, str]
    '''

    pass


def select_all(action: typing.Union[int, str] = 'TOGGLE'):
    '''Select or deselect all strips 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: typing.Union[int, str]
    '''

    pass


def select_box(xmin: int = 0,
               xmax: int = 0,
               ymin: int = 0,
               ymax: int = 0,
               wait_for_input: bool = True,
               mode: typing.Union[int, str] = 'SET',
               tweak: bool = False):
    '''Select strips using box selection 

    :param xmin: X Min 
    :type xmin: int
    :param xmax: X Max 
    :type xmax: int
    :param ymin: Y Min 
    :type ymin: int
    :param ymax: Y Max 
    :type ymax: int
    :param wait_for_input: Wait for Input 
    :type wait_for_input: bool
    :param mode: ModeSET Set, Set a new selection.ADD Extend, Extend existing selection.SUB Subtract, Subtract existing selection. 
    :type mode: typing.Union[int, str]
    :param tweak: Tweak, Operator has been activated using a tweak event 
    :type tweak: bool
    '''

    pass


def select_grouped(type: typing.Union[int, str] = 'TYPE',
                   extend: bool = False,
                   use_active_channel: bool = False):
    '''Select all strips grouped by various properties 

    :param type: TypeTYPE Type, Shared strip type.TYPE_BASIC Global Type, All strips of same basic type (Graphical or Sound).TYPE_EFFECT Effect Type, Shared strip effect type (if active strip is not an effect one, select all non-effect strips).DATA Data, Shared data (scene, image, sound, etc.).EFFECT Effect, Shared effects.EFFECT_LINK Effect/Linked, Other strips affected by the active one (sharing some time, and below or effect-assigned).OVERLAP Overlap, Overlapping time. 
    :type type: typing.Union[int, str]
    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: bool
    :param use_active_channel: Same Channel, Only consider strips on the same channel as the active one 
    :type use_active_channel: bool
    '''

    pass


def select_handles(side: typing.Union[int, str] = 'BOTH'):
    '''Select gizmo handles on the sides of the selected strip 

    :param side: Side, The side of the handle that is selected 
    :type side: typing.Union[int, str]
    '''

    pass


def select_less():
    '''Shrink the current selection of adjacent selected strips 

    '''

    pass


def select_linked():
    '''Select all strips adjacent to the current selection 

    '''

    pass


def select_linked_pick(extend: bool = False):
    '''Select a chain of linked strips nearest to the mouse pointer 

    :param extend: Extend, Extend the selection 
    :type extend: bool
    '''

    pass


def select_more():
    '''Select more strips adjacent to the current selection 

    '''

    pass


def slip(offset: int = 0):
    '''Trim the contents of the active strip 

    :param offset: Offset, Offset to the data of the strip 
    :type offset: int
    '''

    pass


def snap(frame: int = 0):
    '''Frame where selected strips will be snapped 

    :param frame: Frame, Frame where selected strips will be snapped 
    :type frame: int
    '''

    pass


def sound_strip_add(
        filepath: str = "",
        files: typing.List['bpy.types.OperatorFileListElement'] = None,
        hide_props_region: bool = True,
        filter_blender: bool = False,
        filter_backup: bool = False,
        filter_image: bool = False,
        filter_movie: bool = False,
        filter_python: bool = False,
        filter_font: bool = False,
        filter_sound: bool = True,
        filter_text: bool = False,
        filter_archive: bool = False,
        filter_btx: bool = False,
        filter_collada: bool = False,
        filter_alembic: bool = False,
        filter_folder: bool = True,
        filter_blenlib: bool = False,
        filemode: int = 9,
        relative_path: bool = True,
        display_type: typing.Union[int, str] = 'DEFAULT',
        sort_method: typing.Union[int, str] = 'FILE_SORT_ALPHA',
        frame_start: int = 0,
        channel: int = 1,
        replace_sel: bool = True,
        overlap: bool = False,
        cache: bool = False,
        mono: bool = False):
    '''Add a sound strip to the sequencer 

    :param filepath: File Path, Path to file 
    :type filepath: str
    :param files: Files 
    :type files: typing.List['bpy.types.OperatorFileListElement']
    :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings 
    :type hide_props_region: bool
    :param filter_blender: Filter .blend files 
    :type filter_blender: bool
    :param filter_backup: Filter .blend files 
    :type filter_backup: bool
    :param filter_image: Filter image files 
    :type filter_image: bool
    :param filter_movie: Filter movie files 
    :type filter_movie: bool
    :param filter_python: Filter python files 
    :type filter_python: bool
    :param filter_font: Filter font files 
    :type filter_font: bool
    :param filter_sound: Filter sound files 
    :type filter_sound: bool
    :param filter_text: Filter text files 
    :type filter_text: bool
    :param filter_archive: Filter archive files 
    :type filter_archive: bool
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param relative_path: Relative Path, Select the file relative to the blend file 
    :type relative_path: bool
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_VERTICAL Short List, Display files as short list.LIST_HORIZONTAL Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: typing.Union[int, str]
    :param sort_method: File sorting modeFILE_SORT_ALPHA Name, Sort the file list alphabetically.FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.FILE_SORT_TIME Modified Date, Sort files by modification time.FILE_SORT_SIZE Size, Sort files by size. 
    :type sort_method: typing.Union[int, str]
    :param frame_start: Start Frame, Start frame of the sequence strip 
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into 
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection 
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don’t correct overlap on new sequence strips 
    :type overlap: bool
    :param cache: Cache, Cache the sound in memory 
    :type cache: bool
    :param mono: Mono, Merge all the sound’s channels into one 
    :type mono: bool
    '''

    pass


def strip_jump(next: bool = True, center: bool = True):
    '''Move frame to previous edit point 

    :param next: Next Strip 
    :type next: bool
    :param center: Use strip center 
    :type center: bool
    '''

    pass


def strip_modifier_add(type: typing.Union[int, str] = 'COLOR_BALANCE'):
    '''Add a modifier to the strip 

    :param type: Type 
    :type type: typing.Union[int, str]
    '''

    pass


def strip_modifier_copy(type: typing.Union[int, str] = 'REPLACE'):
    '''Copy modifiers of the active strip to all selected strips 

    :param type: TypeREPLACE Replace, Replace modifiers in destination.APPEND Append, Append active modifiers to selected strips. 
    :type type: typing.Union[int, str]
    '''

    pass


def strip_modifier_move(name: str = "Name",
                        direction: typing.Union[int, str] = 'UP'):
    '''Move modifier up and down in the stack 

    :param name: Name, Name of modifier to remove 
    :type name: str
    :param direction: TypeUP Up, Move modifier up in the stack.DOWN Down, Move modifier down in the stack. 
    :type direction: typing.Union[int, str]
    '''

    pass


def strip_modifier_remove(name: str = "Name"):
    '''Remove a modifier from the strip 

    :param name: Name, Name of modifier to remove 
    :type name: str
    '''

    pass


def swap(side: typing.Union[int, str] = 'RIGHT'):
    '''Swap active strip with strip to the right or left 

    :param side: Side, Side of the strip to swap 
    :type side: typing.Union[int, str]
    '''

    pass


def swap_data():
    '''Swap 2 sequencer strips 

    '''

    pass


def swap_inputs():
    '''Swap the first two inputs for the effect strip 

    '''

    pass


def unlock():
    '''Unlock strips so they can be transformed 

    '''

    pass


def unmute(unselected: bool = False):
    '''Unmute (un)selected strips 

    :param unselected: Unselected, Unmute unselected rather than selected strips 
    :type unselected: bool
    '''

    pass


def view_all():
    '''View all the strips in the sequencer 

    '''

    pass


def view_all_preview():
    '''Zoom preview to fit in the area 

    '''

    pass


def view_frame():
    '''Reset viewable area to show range around current frame 

    '''

    pass


def view_ghost_border(xmin: int = 0,
                      xmax: int = 0,
                      ymin: int = 0,
                      ymax: int = 0,
                      wait_for_input: bool = True):
    '''Set the boundaries of the border used for offset-view 

    :param xmin: X Min 
    :type xmin: int
    :param xmax: X Max 
    :type xmax: int
    :param ymin: Y Min 
    :type ymin: int
    :param ymax: Y Max 
    :type ymax: int
    :param wait_for_input: Wait for Input 
    :type wait_for_input: bool
    '''

    pass


def view_selected():
    '''Zoom the sequencer on the selected strips 

    '''

    pass


def view_toggle():
    '''Toggle between sequencer views (sequence, preview, both) 

    '''

    pass


def view_zoom_ratio(ratio: float = 1.0):
    '''Change zoom ratio of sequencer preview 

    :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out 
    :type ratio: float
    '''

    pass
