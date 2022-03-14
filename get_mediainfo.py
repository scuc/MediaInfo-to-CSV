#!/usr/bin/env python3

from pymediainfo import MediaInfo

def get_mediainfo(source_path, mp4):
    '''
    Use pymediainfo lib to extract the MP4 file info.
    Pass these values back to the concat and downcovert.
    '''
    mp4_dict = {}

    # mp4_filepath = source_path + mp4_file
    mp4_filepath = mp4
    media_info = MediaInfo.parse(mp4_filepath)

    for track in media_info.tracks:
        if track.track_type == 'Video':
            mp4_dict.update(v_format = track.format)
            mp4_dict.update(v_info = track.format_info)
            mp4_dict.update(v_profile = track.format_profile)
            mp4_dict.update(v_settings = track.format_settings)
            mp4_dict.update(v_settings_cabac = track.format_settings_cabac)
            mp4_dict.update(v_settings_reframes = track.format_settings_reframes)
            mp4_dict.update(v_format_settings_gop = track.format_settings_gop)
            mp4_dict.update(v_codec_id = track.codec_id)
            mp4_dict.update(v_codec_id_info = track.codec_id_info)
            mp4_dict.update(v_duration = track.duration)
            mp4_dict.update(v_bit_rate_mode = track.bit_rate_mode)
            mp4_dict.update(v_bit_rate = track.bit_rate)
            mp4_dict.update(v_max_bit_rate = track.maximum_bit_rate)
            mp4_dict.update(v_frame_rate = track.frame_rate)
            mp4_dict.update(v_frame_rate_mode = track.frame_rate_mode)
            mp4_dict.update(v_width = track.width)
            mp4_dict.update(v_height = track.height)
            mp4_dict.update(v_rotation = track.rotation)
            mp4_dict.update(v_display_aspect_ratio = track.display_aspect_ratio)
            mp4_dict.update(v_standard = track.standard)
            mp4_dict.update(v_color_space = track.color_space)
            mp4_dict.update(v_chroma_sub = track.chroma_subsampling)
            mp4_dict.update(v_bit_depth = track.bit_depth)
            mp4_dict.update(v_scan_type = track.scan_type)
            mp4_dict.update(v_encoded_date = track.encoded_date)

        if track.track_type == 'Audio':
            mp4_dict.update(a_format = track.format)
            mp4_dict.update(a_format_info = track.format_info)
            mp4_dict.update(a_format_profile = track.format_profile)
            mp4_dict.update(a_codec_id = track.codec_id)
            mp4_dict.update(a_duration = track.duration)
            mp4_dict.update(a_bit_rate_mode = track.bit_rate_mode)
            mp4_dict.update(a_bit_rate = track.bit_rate)
            mp4_dict.update(a_max_bit_rate = track.maximum_bit_rate)
            mp4_dict.update(a_channel_positions = track.channel_positions)
            mp4_dict.update(a_sampling_rate = track.sampling_rate)
            mp4_dict.update(a_compression_mode = track.compression_mode)

    # print("="*20)
    # print(mp4_dict)
    # print("="*20)

    return mp4_dict
