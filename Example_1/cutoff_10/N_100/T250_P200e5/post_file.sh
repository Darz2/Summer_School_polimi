#!/bin/bash

txt_files=(output/*.txt)
input_file="${txt_files[0]}"
output_file="output_data.csv"
echo "cycle density energy" > "$output_file"


awk '
/^(Initialization: )?Current cycle:/ {
    match($0, /Current cycle: *([0-9]+)/, m)
    cycle = m[1]
}

/^[[:space:]]*density:[[:space:]]*/ {
    match($0, /density:[[:space:]]*([0-9.eE+-]+)/, d)
    if (d[1] != "") density = d[1]
}

/^Total potential energy\/kʙ/ {
    match($0, /Total potential energy\/kʙ[[:space:]]*([-0-9.eE+]+)/, e)
    if (e[1] != "") energy = e[1]
}

# If all values are available, print and reset.
(cycle != "" && density != "" && energy != "") {
    print cycle, density, energy
    cycle = ""; density = ""; energy = ""
}
' "$input_file" >> "$output_file"