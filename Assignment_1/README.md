# Assignment 1: Renaming All Files in a Folder Sequentially

## Objective

Rename all files in a specified folder sequentially while keeping the original file extensions intact.

## Requirements

- Input: Path to a folder specified by the user.
- Output: Files renamed in the format `1.ext`, `2.ext`, etc., preserving the original file extensions.
- Ignore directories or non-file items.
- Handle invalid folder paths and permission issues gracefully.
- Rename files in sorted order (alphabetically).
- Skip renaming if the folder is empty.

## Steps

1. **Input Parsing**

   - Prompt user for folder path.
   - Validate folder existence.

2. **File Listing**

   - List all regular files in the folder.
   - Exclude subdirectories or hidden files.

3. **Renaming Files**

   - Rename files starting from `1.ext` to `n.ext`.

4. **Error Handling**
   - Handle invalid paths and permission issues.

## Execution Steps

1. Run the script using the command: `python rename_files.py`
2. Enter the folder path when prompted.
3. Check the folder to see renamed files.

## Example

### Input:

```
my_folder/
├── image1.jpg
├── document.txt
├── report.pdf
├── notes.docs
├── music.mp3
```

### Output:

```
my_folder/
├── 1.jpg
├── 2.txt
├── 3.pdf
├── 4.docs
├── 5.mp3
```
