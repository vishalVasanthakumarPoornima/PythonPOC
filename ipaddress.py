import ipaddress

def ipaddress_validation(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False

if ipaddress_validation(input("Please enter your ip address: ")):
    print("The ip address is valid.")
else:
    print("The ip address is not valid.")
