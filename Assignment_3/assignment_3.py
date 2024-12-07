from PIL import Image

def create_collage(image_paths, output_file="collage.jpg"):
    if len(image_paths) != 4:
        print("Error: Exactly 4 images are required.")
        return
    
    images = []
    try:
        for path in image_paths:
            img = Image.open(path)
            images.append(img)
    except Exception as e:
        print(f"Error loading images: {e}")
        return
    
    # Resize images to the same size
    width, height = images[0].size
    for i in range(len(images)):
        images[i] = images[i].resize((width, height))
    
    # Create a blank image for the collage
    collage_width = width * 2
    collage_height = height * 2
    collage = Image.new('RGB', (collage_width, collage_height))
    
    # Arrange images in a 2x2 grid
    collage.paste(images[0], (0, 0))
    collage.paste(images[1], (width, 0))
    collage.paste(images[2], (0, height))
    collage.paste(images[3], (width, height))
    
    try:
        collage.save(output_file)
        print(f"Collage created successfully: {output_file}")
    except Exception as e:
        print(f"Error saving collage: {e}")

# Example Usage
image_files = [
    input("Enter the path to image 1: "),
    input("Enter the path to image 2: "),
    input("Enter the path to image 3: "),
    input("Enter the path to image 4: ")
]
create_collage(image_files)
