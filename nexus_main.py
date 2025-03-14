import json

def main():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    
    print("🔥 Nexus Éter Ativado 🚀")
    print(f"Modo de operação: {config.get('mode', 'padrão')}")

if __name__ == "__main__":
    main()
