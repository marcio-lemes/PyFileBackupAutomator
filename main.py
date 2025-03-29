from pathlib import Path
from zipfile import ZipFile
from datetime import date, datetime
import shutil
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

today = date.today() #Obtem a data atual
hour = datetime.now().strftime("%H:%M") #Obtem a hora atual e formata (hh:mm) 
formatted_date = today.strftime("%d.%m.%Y") #Formata a data atual

def get_folders():
    """
    Solicita para o usuário os caminhos das pastas de origem e destino.
    
    Retorna:
    Uma tupla com um par (origin_folder, destination_folder) como objetos Path.
    None caso os caminhos inseridos forem inválidos.    
    """
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

#Função para exibir o menu de opções
def show_menu():
    print("\nMenu de opções:")
    print("1 - Fazer backup completo (todos os arquivos) - Apenas uma vez.")
    print("2 - Escolha essa opção para compactar os arquivos antes de enviar.")
    print("3 - Fazer backup agendado.")
    print("4 - Sair")
    

def compress_files(origin_folder, zipname = f"backup-{formatted_date}.zip"):
    """
    Compacta todos os arquivos da pasta de origem em um arquivo ZIP criado.
    
    Args:
    origin_folder: Objeto Path contendo o caminho completo da pasta de origem.
    zipname = String que representa o nome do arquivo ZIP a ser criado.
    
    Retorna o caminho do arquivo ZIP que vai ser criado.
    """
    files = [file for file in origin_folder.iterdir() if file.is_file()]
    zip_path = origin_folder / zipname
    
    with ZipFile(zip_path, 'w') as zip_file:
        for file in files:
            zip_file.write(file)
            print(f"Arquivo '{file.name}' adicionado ao ZIP.")
    print(f"Arquivo zip gerado com sucesso em: {zip_path}.")
    return zip_path
    
def backup_files(origin_folder, destination_folder, compress):
    """
    Faz o backup dos arquivos da pasta de origem para a pasta de destino.
    
    Args:
    origin_folder: Objeto Path contendo o caminho completo da pasta de origem.
    destination_folder: Objeto Path contendo o caminho completo da pasta de destino.
    compress: Variável que define se os arquivos vão ser compactados ou não (True/False).
    
    Gera um arquivo.txt log que registra os detalhes do backup.
    """
    files = [file for file in origin_folder.iterdir() if file.is_file()]
    if compress:
        zip_path = compress_files(origin_folder)
        shutil.move(zip_path, destination_folder / zip_path.name)
        print(f"Arquivo movido para a pasta {destination_folder} com sucesso!")
    else:
        for file in files:
            shutil.copy(file, destination_folder / file.name )
            print(f"Arquivo '{file.name}' movido para {destination_folder}")
    
    #Gera o arquivo de log
    log_path = Path('./backup-logs.txt')
    with log_path.open('w', encoding='utf-8') as log_file:
        log_file.write(f"Às {hour} da data {formatted_date} foram salvos na pasta {destination_folder} os arquivos:\n")
        for i, file in enumerate(files, start=1):
            log_file.write(f"{i} - {file.name}\n")
        print(f"\nLog de backup gerado em: {log_path}")
        
def schedule_backup(origin_folder, destination_folder, compress):
    print("\nQual o período que o backup deve ser efetuado?")
    print("1 - Diariamente")
    print("2 - Semanalmente")
    print("3 - Mensalmente")

    try:
        interval_option = int(input("> "))
    except ValueError:
        print("\nEntrada deve ser um número.")
        return
    
    if interval_option == 1:
        interval = 24 * 60 * 60  # Diariamente
    elif interval_option == 2:
        interval = 7 * 24 * 60 * 60  # Semanalmente
    elif interval_option == 3:
        interval = 30 * 24 * 60 * 60  # Mensalmente
    else:
        print("\nOpção inválida.")
        return
    
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        backup_files, 
        trigger= IntervalTrigger(seconds=interval), 
        args=[origin_folder, destination_folder, compress]
        )
    
    scheduler.start()
    print(f"\nBackup agendado para ser executado a cada {interval / 3600} horas")
    print(f"\nPressione Ctrl+C para encerrar o programa.")
    
    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("\nAgendador encerrado.")