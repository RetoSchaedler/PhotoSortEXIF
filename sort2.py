import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import easygui


def handle_image(file, original_file_name, targetDirectory):
    image = Image.open(file)

    # Lesen der EXIF-Daten im Bild
    exif_data = image._getexif()
    
    # Check ob Bilder EXIF Daten haben
    if exif_data is not None:
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            if tag_name == 'DateTime':
                date_time = value.replace(':', '-').replace(' ', '_')
                # Entfernen der Dateierweiterung vom Originaldateinamen
                base_name = os.path.splitext(original_file_name)[0]
                new_file_name = f"{date_time}_{base_name}.JPG"
                shutil.copy2(file, targetDirectory+'/'+new_file_name)  # Kopieren der Datei

def main():
    # Öffnet einen Dialog zur Auswahl des Quell Ordners
    directory = easygui.diropenbox(title="Wählen Sie den Quell-Ordner mit den JPG Dateien.")
    # Öffnet einen Dialog zur Auswahl des Ziel Ordners
    targetDirectory= easygui.diropenbox(title="Wählen Sie einen leeren Ziel-Ordner aus, wo die sortierten JPG Dateien gespeichert werden.")
    
    for file_name in os.listdir(directory):
        if file_name.lower().endswith('.jpg') or file_name.lower().endswith('.jpeg'):
            handle_image(f"{directory}/{file_name}", file_name, targetDirectory)

if __name__ == "__main__":
    main()
