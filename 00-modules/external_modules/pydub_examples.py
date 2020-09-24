# pip install pydub
# https://github.com/jiaaro/pydub


# example on github

from pydub import AudioSegment

song = AudioSegment.from_wav("never_gonna_give_you_up.wav")
song = AudioSegment.from_mp3("never_gonna_give_you_up.mp3")
mp4_version = AudioSegment.from_file("never_gonna_give_you_up.mp4", "mp4")


# Slice audio:
# pydub does things in milliseconds
ten_seconds = 10 * 1000
first_10_seconds = song[:ten_seconds]
last_5_seconds = song[-5000:]

# Make the beginning louder and the end quieter
# boost volume by 6dB
beginning = first_10_seconds + 6

# reduce volume by 3dB
end = last_5_seconds - 3

# Concatenate audio (add one file to the end of another)
without_the_middle = beginning + end

# How long is it?
without_the_middle.duration_seconds == 15.0

# AudioSegments are immutable
# song is not modified
backwards = song.reverse()

# Crossfade (again, beginning and end are not modified)
# 1.5 second crossfade
with_style = beginning.append(end, crossfade=1500)

# Repeat
# repeat the clip twice
do_it_over = with_style * 2

# Fade (note that you can chain operations because everything returns an AudioSegment)
# 2 sec fade in, 3 sec fade out
awesome = do_it_over.fade_in(2000).fade_out(3000)

# Save the results (again whatever ffmpeg supports)
awesome.export("mashup.mp3", format="mp3")

# Save the results with tags (metadata)
awesome.export("mashup.mp3", format="mp3", tags={'artist': 'Various artists', 'album': 'Best of 2011', 'comments': 'This album is awesome!'})

# You can pass an optional bitrate argument to export using any syntax ffmpeg supports.
awesome.export("mashup.mp3", format="mp3", bitrate="192k")











