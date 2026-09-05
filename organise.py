from pathlib import Path
import shutil
folder = Path("project")

categories = {
"image" : [".jpeg", ".png"],
"video" : [".mp4", ".mkv"],
"music" : [".mp3", ".wav"],
"document":[".pdf",".docx",".txt",".csv"],
}

if not folder.exists():
    print("Folder stupid-file does not exist")
    exit()

for file in folder.iterdir():
    if not file.is_file():
        continue
    ext = file.suffix.lower()
    category = "others"
    for folder_name , extensions in categories.items():
        if ext in extensions:
            category = folder_name
            break
    print(file.name, "->", category)

    destination_folder = folder/category
    destination_folder.mkdir(exist_ok=True)

    destination_file = destination_folder/file.name

    if destination_file.exists():
        counter =1
        while True : 
            new_name=file.stem + "_"+ str(counter)+ file.suffix
            new_destination= destination_folder/new_name

            if not new_destination.exists():
                destination_file = new_destination
                break
        counter +=1
        
    shutil.move(str(file),str(destination_file))
    print(f"moved: {file.name} -> {category} ")

print("FILE ORGANIZATION COMPLETED!")