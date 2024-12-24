import os

def create_day_subfolders(parent_folders, days=25):
    os.chdir("..") # 1 folder up
    for year in parent_folders:
        if not os.path.exists(year):
            print(f"Folder '{year}' does not exist. Skipping...")
            continue
        
        print(f"\nProcessing year folder: {year}")
        
        for day in range(1, days + 1):
            day_folder = f"Day_{day:02d}"  
            path = os.path.join(year, day_folder)

            if os.path.exists(path):
                print(f"Skipping existing folder: {path}")
            else:
                os.makedirs(path)
                print(f"Created: {path}")

if __name__ == "__main__":
    year_folders = [str(year) for year in range(2015, 2025)]  # Folder with year number needs to exist
    create_day_subfolders(year_folders)
