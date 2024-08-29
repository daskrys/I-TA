# VPC Flow Log Parser

### Description
Program takes VPC flow logs as a text file, parses the logs into a look up table, and exports it as a .csv:
- Destination Port, Protocol, Tag
- Tag, Count
- Port, Protocol, Count

### Requirements
- Python 3.12 or above

### Assumptions

1. The program only supports default log format, not custom and the only version that is supported is 2
2. It is up to me to decide *how* to generate tags for the program. I chose to generate tags based on the following

- port number is over 49151
- port is a common email port
- remote desktop protocol port number 3389
- protocol is udp or tcp and *common* port
- protocol is udp or tcp and *uncommon* port
- protocol is *not* udp or tcp

Reference used to define [Common Network Ports](https://opensource.com/article/18/10/common-network-ports)

3. Only use the first 10 IP protocol numbers as well as IPv6 and UDP
4. The program does not take input for the text file or otherwise. It can be changed before running the program at the top of ```main.py``` under the ```FILE_PATH``` variable to desired path
5. Operating System: macOS, Linux

Reference used for [Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)

### Usage
1. Clone
    ```bash
    git clone https://github.com/daskrys/I-TA
    ```
2. Navigate to project directory:
    ```bash
    cd I-TA
    ```
3. Run
    ```bash
    python3 main.py
    ```

### Testing Summary

Testing for this program was done using the provided sample flow logs by:

1. Testing using provided logs
2. Copying the logs multiple times to ensure program counts correctly
3. Making adjustments to ensure logs fell into one of the 6 tags  
