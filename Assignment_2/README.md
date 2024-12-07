# Assignment 2: Zipping a Folder

## Objective

Compress all files and subdirectories inside a folder into a `.zip` archive.

## Requirements

- Input: Path to the folder specified by the user.
- Output: A `.zip` file named after the folder (e.g., `my_folder.zip`).
- Preserve folder structure and handle invalid folder paths.
- Create an empty `.zip` file if the folder is empty.
- Use standard ZIP compression.

## Steps

1. **Input Parsing**

   - Prompt user for folder path.
   - Validate folder existence.

2. **Directory Traversal**

   - Traverse the folder and subdirectories to list all contents.

3. **Zipping**

   - Create a `.zip` file preserving the structure.

4. **Error Handling**
   - Handle invalid paths, permission issues, and file conflicts.

## Execution Steps

1. Run the script using the command: `python zip_folder.py`
2. Enter the folder path when prompted.
3. Locate the `.zip` file in the same directory as the folder.

## Example

### Input:

```
my_folder/
├── file1.txt
├── file2.txt
└── subfolder/
    ├── file3.txt
    └── file4.txt
```

### Output:

```
my_folder.zip
```
