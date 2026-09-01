import json

from checks import run_security_checks, check_firewall

def load_configuration():
    with open("data/config.json", "r") as file:
        configuration = json.load(file)
        
    return configuration

def main():
    configuration = load_configuration() 
    
    findings = run_security_checks(configuration, [check_firewall])
    
    print("Security checks completed.")
    print(f"Findings:{len(findings)}")
    for finding in findings:
        print(finding)
    
    

if __name__ == "__main__":
    main()