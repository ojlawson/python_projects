import re


def convert_to_bind_format(input_file, output_file):
    """
        Converts DNS records from a custom format to BIND-compatible format.

        Parameters:
        - input_file: The path to the input file containing DNS records.
        - output_file: The path to the output file to write BIND-formatted records.
    """

    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        file.write("; Name                  Type   Target\n")
        for line in lines[1:]:
            parts = line.strip().split('\t')
            if len(parts) < 3:
                continue
            name, type, data = parts[0], parts[1], parts[2]
            if "SOA" in type or "NS" in type:
                continue
            if name == "(same as parent folder)":
                name = "@"
            type = re.sub(r'Alias \(CNAME\)', 'CNAME', type)
            type = re.sub(r'Host \(A\)', 'A', type)
            data = data.replace('static', '').strip()
            file.write(f"{name}\tIN\t{type}\t{data}\n")


# Specify input and output file names
convert_to_bind_format('rp-stage.zone', 'output.zone')
