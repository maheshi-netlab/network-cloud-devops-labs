hostname = "fw-lab-01"
management_ip = "192.168.1.10"
port = 443
cpu_usage = 72.5
firewall_enabled = True
allowed_services = ["SSH", "HTTPS", "DNS"]

firewall = {
    "hostname": hostname,
    "management_ip": management_ip,
    "vendor": "Palo Alto",
    "port": port
}

print("Firewall Data Types")
print("====================")

print("Hostname:", hostname, type(hostname))
print("Management IP:", management_ip, type(management_ip))
print("Port:", port, type(port))
print("CPU Usage:", cpu_usage, type(cpu_usage))
print("Firewall Enabled:", firewall_enabled, type(firewall_enabled))
print("Allowed Services:", allowed_services, type(allowed_services))
print("Firewall Inventory:", firewall, type(firewall))
