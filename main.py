from pathlib import Path
from zipfile import ZipFile
from datetime import date, datetime
import shutil

today = date.today()
hour = datetime.now().strftime("%H:%M")
formatted_date = today.strftime("%d.%m.%Y")

def get_folders():
    origin_folder_path = input("Insira o caminho da pasta de origem:\n")
    origin_folder = Path(origin_folder_path)
    if not origin_folder.exists() or not origin_folder.is_dir():
        print("Caminho inválido. Certifique-se de que é uma pasta existente.")
        return None
    
    destination_folder_path = input("Insira o caminho da pasta de destino:\n")
    destination_folder = Path(destination_folder_path)
    if not destination_folder.exists() or not destination_folder.is_dir():
        print("Caminho inválido. Certifique-se de que é uma pasta existente.")
        return None
    
    return origin_folder, destination_folder


def show_menu():
    print("\nMenu de opções:")
    print("1 - Fazer backup completo (todos os arquivos).")
    print("2 - Escolha essa opção para compactar os arquivos antes de enviar.")
    print("3 - Sair")
    

def compress_files(origin_folder, zipname = f"backup-{formatted_date}.zip"):
    files = [file for file in origin_folder.iterdir() if file.is_file()]
    zip_path = origin_folder / zipname
    
    with ZipFile(zip_path, 'w') as zip_file:
        for file in files:
            zip_file.write(file)
            print(f"Arquivo '{file.name}' adicionado ao ZIP.")
    print(f"Arquivo zip gerado com sucesso em: {zip_path}.")
    return zip_path
    
def backup_files(origin_folder, destination_folder, compress):
    files = [file for file in origin_folder.iterdir() if file.is_file()]
    if compress:
        zip_path = compress_files(origin_folder)
        shutil.move(zip_path, destination_folder / zip_path.name)
        print(f"Arquivo movido para a pasta {destination_folder} com sucesso!")
    else:
        for file in files:
            shutil.copy(file, destination_folder / file.name )
            print(f"Arquivo '{file.name}' movido para {destination_folder}")
    
    log_path = Path('./backup-logs.txt')
    with log_path.open('w', encoding='utf-8') as log_file:
        log_file.write(f"Às {hour} da data {formatted_date} foram salvos na pasta {destination_folder} os arquivos:\n")
        for i, file in enumerate(files, start=1):
            log_file.write(f"{i} - {file.name}\n")
        print(f"Log de backup gerado em: {log_path}")