from main import show_menu, get_folders, compress_files, backup_files

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
                print("Saindo!")
                break
            case 4:
                print("Opção inválida.")