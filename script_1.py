import subprocess, os, re

def findFilenames():
    list_temp = os.listdir("/FILE/PATH/HERE/Script_IN/")
    print(list)
    return list_temp

def encode(ffmpeg_cmd):
    subprocess.call(ffmpeg_cmd, shell=True)
    print(ffmpeg_cmd)

def getEXT(sourcename):
    source_index_ext = sourcename.find(".")
    source_ext = sourcename[source_index_ext:]
    basename = sourcename.replace(source_ext, '.mov')
    return basename

def run(source):
    if source == '.DS_Store':
        pass
    else:
        basename = getEXT(source)
        cmd = 'ffmpeg -analyzeduration 100M -probesize 100M -y -i "/FILE/PATH/HERE/Script_IN/' + source + '" -vcodec prores_ks -profile:v 3 -pix_fmt yuv422p10le -color_primaries bt2020 -color_trc smpte2084 -colorspace 9 -vendor ap10 -acodec pcm_s16be "/FILE/PATH/HERE/Script_OUT/' + basename +'"'
        encode(cmd)
        filepath_in = '/FILE/PATH/HERE/Script_IN/' + source
        filepath_out = '/FILE/PATH/HERE/Script_OUT/' + source
        os.rename(filepath_in, filepath_out)
        print(source + " has been encoded.")

def getSize(filepath):
    file_info = os.stat('/FILE/PATH/HERE/Script_IN/' + filepath)
    return file_info.st_size
