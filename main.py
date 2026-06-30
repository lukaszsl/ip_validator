from ip_validator import IPValidator

def main():
    validator = IPValidator()

    while True:
        ip_address = input("Enter an IP address to validate (or type 'exit' to quit): ")
        if ip_address.lower() == 'exit':
            print("Exiting the IP Validator.")
            break
        
        if validator.is_valid_ipv4(ip_address):
            print(f"{ip_address} is a valid IPv4 address.")
        else:
            print(f"{ip_address} is NOT a valid IPv4 address.")

if __name__ == "__main__":
    main()  