# install moviepy

from moviepy.editor import VideoFileClip

clip = VideoFileClip("file.mp4")
clip.write_gif('file.gif', fps=20)

'''
clip = (VideoFileClip("PATH NAME").subclip((START TIME),(END TIME)) .resize(ACCORDING TO THE USER WISH)) 
clip.write_gif("output.gif")
'''