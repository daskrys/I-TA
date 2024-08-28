import csv

parsed_logs = []
lookup_table = {}
lookup_count = {}
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

EMAIL_PORTS = [109, 143, 158, 209, 993]
COMMON_PORTS = [0, 20, 21, 22, 23, 25, 53, 80, 110, 119, 123, 161, 194, 443]

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

def assign_tag(port, protocol):

    if port >= 49152:
        return "private"
    elif port in EMAIL_PORTS:
        return "email"
    elif port == 3389:
        return "sv_P5"
    elif (protocol == "UDP") or (protocol == "TCP"):
        if port in COMMON_PORTS:
            return "sv_P1"
        else:
            return "sv_P2"
    elif port in COMMON_PORTS:
        return "sv_P3"
    else:
        return "sv_P4"

def export_to_csv():

    tags = {}

    with open("logs.csv", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(['dstport', 'protocol', 'tag'])

        for temp in lookup_table:
            port, protocol = temp
            tag, count = lookup_table[temp]

            if tag in tags:
                tags[tag] += 1
            else:
                tags[tag] = 1

            csvwriter.writerow([port, protocol, tag])

        csvwriter.writerow(['Tag', 'Count'])

        for t in tags:
            csvwriter.writerow([t, tags[t]])

        csvwriter.writerow(['Port', 'Protocol', 'Count'])

        for temp in lookup_table:
            port, protocol = temp
            tag, count = lookup_table[(port, protocol)]
            csvwriter.writerow([port, protocol, count])
        

if __name__ == "__main__":
    read_data()

    for log in parsed_logs:
        dstport = log["dstport"]
        protocol_num = log["protocol"]
        protocol = IANA_PROTOCOLS[protocol_num]

        tag = assign_tag(dstport, protocol)
        
        if (dstport, protocol) not in lookup_table:
            lookup_table[(dstport, protocol)] = tag, 1
        else:
            temp, count = lookup_table[(dstport, protocol)]
            lookup_table[(dstport, protocol)] = tag, count + 1

    export_to_csv()