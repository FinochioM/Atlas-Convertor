from PIL import Image, ImageDraw, ImageFont
import os
import PySimpleGUI as sg
def separate_tiles(path, output_dir):
    fontsize = 8

    image = Image.open(path)


    width, height = image.size

    tiles_x = width // 16
    tiles_y = height // 16

    # Create a draw object
    draw = ImageDraw.Draw(image)

    # Load a truetype font
    font = ImageFont.truetype("D:\Atlas-Convertor\helvetica-light-587ebe5a59211.ttf", fontsize)

    for i in range(tiles_y):
        for j in range(tiles_x):
            left = j * 16
            upper = i * 16
            right = left + 16
            lower = upper + 16

            # Draw the index number on the tile
            draw.text((left, upper), str(i * tiles_x + j), fill="#00FFFF", font=font)

    # Save the image with the index numbers
    image.save(os.path.join(output_dir, 'indexed_image.png'))

def main():
    # Define the window's contents
    layout = [[sg.Text("Image Path"), sg.Input(key='-IMAGE-'), sg.FileBrowse()],
              [sg.Text("Output Directory"), sg.Input(key='-OUTDIR-'), sg.FolderBrowse()],
              [sg.Button('Ok'), sg.Button('Cancel')]]

    # Create the window
    window = sg.Window('Tile Separator', layout)

    # Display and interact with the Window
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the Cancel button
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        if event == 'Ok':
            image_path = values['-IMAGE-']
            output_dir = values['-OUTDIR-']
            separate_tiles(image_path, output_dir)
            sg.popup('Operation completed successfully')

    window.close()

if __name__ == '__main__':
    main()