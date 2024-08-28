import csv

parsed_logs = []
FILE_PATH = "logdata.txt"

IANA_PROTOCOLS = {
    "1": "ICMP",
    "2": "IGMP",
    "3": "GGP",
    "4": "IPv4",
    "5": "Stream",
    "6": "TCP",
    "7": "CBT",
    "8": "EGP",
    "9": "IGP",
    "17": "UDP",
    "41": "IPv6",
}

EMAIL = [109, 110, 143, 158, 209, 993]

def parse_line(list):
    return {
        "version": list[0],
        "account_id": list[1],
        "interface_id": list[2],
        "srcaddr": list[3],
        "dstaddr": list[4],
        "srcport": int(list[5]),
        "dstport": int(list[6]),
        "protocol": list[7],
        "packets": int(list[8]),
        "bytes": int(list[9]),
        "start": int(list[10]),
        "end": int(list[11]),
        "action": list[12],
        "log_status": list[13],
    }

def read_data():
    with open(FILE_PATH, 'r') as file:
        for line in file:
            list = line.split()

            if list:
                parse = parse_line(list)
                parsed_logs.append(parse)

if __name__ == "__main__":
    read_data()
    
    for log in parsed_logs:
        dstport = log["dstport"]
        protocol_num = log["protocol"]
        protocol = IANA_PROTOCOLS[protocol_num]

        print(f"{dstport} and {protocol}")