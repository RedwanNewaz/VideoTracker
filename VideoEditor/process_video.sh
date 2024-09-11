#!/bin/bash

# Define variables
input_dir="../results/vid1"
output_filename="../results/vid1.mp4"
input_framerate="30.001580"
output_framerate="30"
resolution="3840:2160"

# Function to process video
process_video() {
    local input_pattern="$1/%04d.png"
    local output="$2"
    
    ffmpeg -framerate "$input_framerate" -i "$input_pattern" \
        -c:v libx265 \
        -pix_fmt yuv420p \
        -vf "scale=$resolution,format=yuv420p" \
        -r "$output_framerate" \
        -color_primaries bt709 \
        -color_trc bt709 \
        -colorspace bt709 \
        -chroma_sample_location left \
        -c:a aac \
        -b:a 192k \
        -ar 48000 \
        -ac 2 \
        "$output"
}

# Main function
process_video "$input_dir" "$output_filename"
