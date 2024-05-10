import re  # regex module


def convert_to_bind_format(input_file, output_file):
    """
        Converts DNS records from a custom format to BIND-compatible format.

        Parameters:
        - input_file: The path to the input file containing DNS records.
        - output_file: The path to the output file to write BIND-formatted records.
    """

    with open(input_file, 'r') as file:  # open input file in read mode
        lines = file.readlines()  # read all lines in file and store in lines variable

    with open(output_file, 'w') as file:  # open/create output file in write mode
        file.write("; Name                  Type   Target\n")  # add required header columns
        for line in lines[1:]:  # skip the header line (start at index 1)
            parts = line.strip().split('\t')  # strip EOL whitespaces and split line based on tabs
            if len(parts) < 3:
                continue  # Skip lines which do not have the 3 required parts
            name, type, data = parts[0], parts[1], parts[2]
            if "SOA" in type or "NS" in type:
                continue  # Skip SOA and NS records
            if name == "(same as parent folder)":  # swap this with @
                name = "@"  # @ is used to denote current origin in DNS
            type = re.sub(r'Alias \(CNAME\)', 'CNAME', type)  # regex to change record type to BIND format
            type = re.sub(r'Host \(A\)', 'A', type)  # regex to change record type to BIND format
            data = data.replace('static', '').strip()  # remove 'static' and trailing whitespaces
            file.write(f"{name}\t300\tIN\t{type}\t{data}\n")  # write the formatted DNS records to the output file


# Specify input and output file names
convert_to_bind_format('input.zone', 'output.zone')
