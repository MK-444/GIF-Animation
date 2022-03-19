from PIL import Image

frames = []

for frame_number in range(0, 122):
    frame = Image.open(f"img/DiscoLightsVidevo_{frame_number}.jpg")
    frames.append(frame)

frames[0].save(
    'animation.gif',
    save_all=True,
    append_images=frames[1:],
    optimize=True,
    duration=1,
    loop=0
)