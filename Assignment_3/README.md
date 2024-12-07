# Assignment 3: Creating a Collage from 4 Images

## Objective

Combine four images into a 2x2 collage and save the result as a new image file.

## Requirements

- Input: Paths to four image files specified by the user.
- Output: A single image file named `collage.jpg`.
- Resize input images to the same dimensions.

## Steps

1. **Input Handling**

   - Prompt user for paths to four images.
   - Validate that the provided files are images.

2. **Image Processing**

   - Resize all images to fit a uniform grid.
   - Arrange images in a 2x2 grid.

3. **Saving the Collage**

   - Save the resulting image as `collage.jpg`.

4. **Error Handling**
   - Handle invalid file paths or unsupported formats.

## Execution Steps

1. Run the script using the command: `python create_collage.py`
2. Enter the paths to the four images when prompted.
3. Locate `collage.jpg` in the output directory.

## Example

### Input:

Paths to:

- `image1.jpg`
- `image2.jpg`
- `image3.jpg`
- `image4.jpg`

### Output:

A collage saved as `collage.jpg`.
