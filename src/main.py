import json

from checks import run_security_checks

def load_configuration():
    with open("data/config.json", "r") as file:
        configuration = json.load(file)
        
    return configuration

def main():
    configuration = load_configuration() 
    
    findings = run_security_checks(configuration, [])
    
    print("Security checks completed.")
    print(f"Findings:{len(findings)}")



if __name__ == "__main__":
    main()