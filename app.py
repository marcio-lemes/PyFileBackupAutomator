from main import show_menu, get_folders, compress_files, backup_files, schedule_backup
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler() #Instância o agendador
scheduler.start() #Inicializa o agendador

compress = False

folders = get_folders()
if folders:
    origin_folder, destination_folder = folders
else:
    print("Erro ao obter os caminhos das pastas")
    
if folders:
    while True:
        show_menu()
        
        try:
            option = int(input("> "))
        except ValueError:
            print("Entrada deve ser um número.")
            continue
        
        match option:
            case 1:
                backup_files(origin_folder, destination_folder, compress)
            case 2:
                compress = True
                print("Os arquivos serão compactados.")
            case 3:
                print("\nQual o período que o backup deve ser efetuado?")
                print("1 - Diariamente")
                print("2 - Semanalmente")
                print("3 - Mensalmente")

                try:
                    interval_option = int(input("> "))
                except ValueError:
                    print("\nEntrada deve ser um número.")
                    continue
                
                if interval_option in [1, 2, 3]:
                    schedule_backup(origin_folder, destination_folder, compress, interval_option, scheduler)
                else:
                    print("Opção inválida.")
                    continue
            case 4:
                print("Saindo!")
                scheduler.shutdown()
                break
            case _:
                print("Opção inválida.")