# -*- coding: utf-8 -*-

from typing import Union


def bake_animation():
    """Update the audio animation cache 

    """

    pass


def mixdown(filepath: str = "",
            check_existing: bool = True,
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
            filter_usd: bool = False,
            filter_folder: bool = True,
            filter_blenlib: bool = False,
            filemode: int = 9,
            relative_path: bool = True,
            display_type: Union[str, int] = 'DEFAULT',
            sort_method: Union[str, int] = 'FILE_SORT_ALPHA',
            accuracy: int = 1024,
            container: Union[str, int] = 'FLAC',
            codec: Union[str, int] = 'FLAC',
            format: Union[str, int] = 'S16',
            bitrate: int = 192,
            split_channels: bool = False):
    """Mix the scene’s audio to a sound file 

    :param filepath: File Path, Path to file 
    :param check_existing: Check Existing, Check and warn on overwriting
    existing files
    :param filter_blender: Filter .blend files
    :param filter_backup: Filter .blend files
    :param filter_image: Filter image files
    :param filter_movie: Filter movie files
    :param filter_python: Filter python files
    :param filter_font: Filter font files
    :param filter_sound: Filter sound files
    :param filter_text: Filter text files
    :param filter_archive: Filter archive files
    :param filter_btx: Filter btx files
    :param filter_collada: Filter COLLADA files
    :param filter_alembic: Filter Alembic files
    :param filter_usd: Filter USD files
    :param filter_folder: Filter folders
    :param filter_blenlib: Filter Blender IDs
    :param filemode: File Browser Mode, The setting for the file browser mode
    to load a .blend file, a library or a special file
    :param relative_path: Relative Path, Select the file relative to the
    blend file
    :param display_type: Display TypeDEFAULT Default, Automatically determine
    display type for files.LIST_VERTICAL Short List, Display files as short
    list.LIST_HORIZONTAL Long List, Display files as a detailed
    list.THUMBNAIL Thumbnails, Display files as thumbnails.
    :param sort_method: File sorting modeFILE_SORT_ALPHA Name, Sort the file
    list alphabetically.FILE_SORT_EXTENSION Extension, Sort the file list by
    extension/type.FILE_SORT_TIME Modified Date, Sort files by modification
    time.FILE_SORT_SIZE Size, Sort files by size.
    :param accuracy: Accuracy, Sample accuracy, important for animation data
    (the lower the value, the more accurate)
    :param container: Container, File formatAC3 ac3, Dolby Digital ATRAC
    3.FLAC flac, Free Lossless Audio Codec.MATROSKA mkv, Matroska.MP2 mp2,
    MPEG-1 Audio Layer II.MP3 mp3, MPEG-2 Audio Layer III.OGG ogg, Xiph.Org
    Ogg Container.WAV wav, Waveform Audio File Format.
    :param codec: Codec, Audio CodecAAC AAC, Advanced Audio Coding.AC3 AC3,
    Dolby Digital ATRAC 3.FLAC FLAC, Free Lossless Audio Codec.MP2 MP2,
    MPEG-1 Audio Layer II.MP3 MP3, MPEG-2 Audio Layer III.PCM PCM, Pulse Code
    Modulation (RAW).VORBIS Vorbis, Xiph.Org Vorbis Codec.
    :param format: Format, Sample formatU8 U8, 8 bit unsigned.S16 S16,
    16 bit signed.S24 S24, 24 bit signed.S32 S32, 32 bit signed.F32 F32,
    32 bit floating point.F64 F64, 64 bit floating point.
    :param bitrate: Bitrate, Bitrate in kbit/s
    :param split_channels: Split channels, Each channel will be rendered into
    a mono file
    """

    pass


def open(filepath: str = "",
         hide_props_region: bool = True,
         filter_blender: bool = False,
         filter_backup: bool = False,
         filter_image: bool = False,
         filter_movie: bool = True,
         filter_python: bool = False,
         filter_font: bool = False,
         filter_sound: bool = True,
         filter_text: bool = False,
         filter_archive: bool = False,
         filter_btx: bool = False,
         filter_collada: bool = False,
         filter_alembic: bool = False,
         filter_usd: bool = False,
         filter_folder: bool = True,
         filter_blenlib: bool = False,
         filemode: int = 9,
         relative_path: bool = True,
         show_multiview: bool = False,
         use_multiview: bool = False,
         display_type: Union[str, int] = 'DEFAULT',
         sort_method: Union[str, int] = 'FILE_SORT_ALPHA',
         cache: bool = False,
         mono: bool = False):
    """Load a sound file 

    :param filepath: File Path, Path to file 
    :param hide_props_region: Hide Operator Properties, Collapse the region
    displaying the operator settings
    :param filter_blender: Filter .blend files
    :param filter_backup: Filter .blend files
    :param filter_image: Filter image files
    :param filter_movie: Filter movie files
    :param filter_python: Filter python files
    :param filter_font: Filter font files
    :param filter_sound: Filter sound files
    :param filter_text: Filter text files
    :param filter_archive: Filter archive files
    :param filter_btx: Filter btx files
    :param filter_collada: Filter COLLADA files
    :param filter_alembic: Filter Alembic files
    :param filter_usd: Filter USD files
    :param filter_folder: Filter folders
    :param filter_blenlib: Filter Blender IDs
    :param filemode: File Browser Mode, The setting for the file browser mode
    to load a .blend file, a library or a special file
    :param relative_path: Relative Path, Select the file relative to the
    blend file
    :param show_multiview: Enable Multi-View
    :param use_multiview: Use Multi-View
    :param display_type: Display TypeDEFAULT Default, Automatically determine
    display type for files.LIST_VERTICAL Short List, Display files as short
    list.LIST_HORIZONTAL Long List, Display files as a detailed
    list.THUMBNAIL Thumbnails, Display files as thumbnails.
    :param sort_method: File sorting modeFILE_SORT_ALPHA Name, Sort the file
    list alphabetically.FILE_SORT_EXTENSION Extension, Sort the file list by
    extension/type.FILE_SORT_TIME Modified Date, Sort files by modification
    time.FILE_SORT_SIZE Size, Sort files by size.
    :param cache: Cache, Cache the sound in memory
    :param mono: Mono, Merge all the sound’s channels into one
    """

    pass


def open_mono(filepath: str = "",
              hide_props_region: bool = True,
              filter_blender: bool = False,
              filter_backup: bool = False,
              filter_image: bool = False,
              filter_movie: bool = True,
              filter_python: bool = False,
              filter_font: bool = False,
              filter_sound: bool = True,
              filter_text: bool = False,
              filter_archive: bool = False,
              filter_btx: bool = False,
              filter_collada: bool = False,
              filter_alembic: bool = False,
              filter_usd: bool = False,
              filter_folder: bool = True,
              filter_blenlib: bool = False,
              filemode: int = 9,
              relative_path: bool = True,
              show_multiview: bool = False,
              use_multiview: bool = False,
              display_type: Union[str, int] = 'DEFAULT',
              sort_method: Union[str, int] = 'FILE_SORT_ALPHA',
              cache: bool = False,
              mono: bool = True):
    """Load a sound file as mono 

    :param filepath: File Path, Path to file 
    :param hide_props_region: Hide Operator Properties, Collapse the region
    displaying the operator settings
    :param filter_blender: Filter .blend files
    :param filter_backup: Filter .blend files
    :param filter_image: Filter image files
    :param filter_movie: Filter movie files
    :param filter_python: Filter python files
    :param filter_font: Filter font files
    :param filter_sound: Filter sound files
    :param filter_text: Filter text files
    :param filter_archive: Filter archive files
    :param filter_btx: Filter btx files
    :param filter_collada: Filter COLLADA files
    :param filter_alembic: Filter Alembic files
    :param filter_usd: Filter USD files
    :param filter_folder: Filter folders
    :param filter_blenlib: Filter Blender IDs
    :param filemode: File Browser Mode, The setting for the file browser mode
    to load a .blend file, a library or a special file
    :param relative_path: Relative Path, Select the file relative to the
    blend file
    :param show_multiview: Enable Multi-View
    :param use_multiview: Use Multi-View
    :param display_type: Display TypeDEFAULT Default, Automatically determine
    display type for files.LIST_VERTICAL Short List, Display files as short
    list.LIST_HORIZONTAL Long List, Display files as a detailed
    list.THUMBNAIL Thumbnails, Display files as thumbnails.
    :param sort_method: File sorting modeFILE_SORT_ALPHA Name, Sort the file
    list alphabetically.FILE_SORT_EXTENSION Extension, Sort the file list by
    extension/type.FILE_SORT_TIME Modified Date, Sort files by modification
    time.FILE_SORT_SIZE Size, Sort files by size.
    :param cache: Cache, Cache the sound in memory
    :param mono: Mono, Mixdown the sound to mono
    """

    pass


def pack():
    """Pack the sound into the current blend file 

    """

    pass


def unpack(method: Union[str, int] = 'USE_LOCAL', id: str = ""):
    """Unpack the sound to the samples filename 

    :param method: Method, How to unpack
    :param id: Sound Name, Sound data-block name to unpack
    """

    pass


def update_animation_flags():
    """Update animation flags 

    """

    pass
