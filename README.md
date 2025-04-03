# Sistema de Backup Automatizado


[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)

## 📝 Descrição
Sistema de backup robusto desenvolvido em Python que oferece:
- Cópia segura de arquivos entre diretórios
- Compactação em formato ZIP
- Agendamento automático (diário/semanal/mensal)
- Geração de logs detalhados

## ✨ Funcionalidades
- **Backup completo** de pastas
- **Compactação** em arquivos ZIP
- **Agendamento flexível** (24h, 7d, 30d)
- **Sistema de logs** com registro de operações
- **Validação** de caminhos e parâmetros

## 🛠 Tecnologias
```python
{
  "Linguagem": "Python 3.8+",
  "Bibliotecas": [
    "APScheduler",
    "pathlib", 
    "zipfile",
    "shutil",
    "datetime"
  ],
  "Práticas": [
    "POO",
    "Tratamento de exceções",
    "CLI",
    "Ambientes virtuais (.venv)"
  ]
}
```

## 🚀 Como Usar
1. Instale as dependências:
```bash
pip install apscheduler
```
2. Execute o sistema:
```bash
python app.py
```
3. Siga o menu interativo.

## 📂 Estrutura do Projeto
- app.py: Ponto de entrada
- main.py: Lógica principal
- .venv/: Ambiente virtual

## Exemplo de uso
### Backup Imediato:
1. Selecione a opção 1 no menu
2. Todos os arquivos serão copiados para a pasta de destino
### Backup Compactado:
1. Selecione a opção 2 para ativar a compactação
2. Execute o backup (opção 1)
3. Arquivos serão compactados em ZIP e este será enviado para a pasta destino
### Backup Agendado:
1. Selecione a opção 3
2. Escolha o intervalo desejado (diário, semanal, mensal)
3. O sistema executará automaticamente o backup nos intervalos configurados

## 🤝 Contato
- Márcio Simões Lemes
- GitHub: marcio-lemes
- Email: devmarciolemes@gmail.com

