import time
import os
import asyncio
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser


async def fix_thumb(thumb):
    width = 0
    height = 0
    try:
        if thumb is not None:
            metadata = extractMetadata(createParser(thumb))
            if metadata.has("width"):
                width = metadata.get("width")
            if metadata.has("height"):
                height = metadata.get("height")
                Image.open(thumb).convert("RGB").save(thumb)
                img = Image.open(thumb)
                img.resize((320, height))
                img.save(thumb, "JPEG")
    except Exception as e:
        print(e)
        thumb = None

    return width, height, thumb


async def take_screen_shot(video_file, output_directory, ttl):
    output_file_name = f"{output_directory}/{time.time()}.jpg"
    file_generator_command = [
        "ffmpeg",
        "-ss",
        str(ttl),
        "-i",
        video_file,
        "-vframes",
        "1",
        output_file_name
    ]
    process = await asyncio.create_subprocess_exec(
        *file_generator_command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    error_response = stderr.decode().strip()
    temp_response = stdout.decode().strip()
    if os.path.lexists(output_file_name):
        return output_file_name
    return None