# Removes unsupported xml tags for old flows, helpful for people using devops center which for screenflows insists on using the latest api version instead of the one the actually is
def modify_xml_file(filename):
    # Read the file contents into a list of lines
    with open(filename, 'r') as f:
        lines = f.readlines()

    # List of placeholders
    placeholders = [
        "InputField", "DropdownBox", "LargeTextArea",
        "RadioButtons", "MultiSelectCheckboxes", "MultiSelectPicklist"
    ]

    # Process the lines
    i = 0
    while i < len(lines) - 1:  # Iterate until second last line, because we are also checking the next line
        line = lines[i].strip()  # Remove leading/trailing whitespace

        # Check if line contains any of the placeholders
        if any(f'<fieldType>{placeholder}</fieldType>' in line for placeholder in placeholders):

            # Check if the next line contains the target string to be removed
            if '<inputsOnNextNavToAssocScrn>' in lines[i+1]:
                lines.pop(i+1)  # Remove the line
                continue  # No need to increment 'i', because we removed a line and want to process the same index again

        i += 1

    # Write the modified lines back to the file
    with open(filename, 'w') as f:
        f.writelines(lines)

# Call the function
modify_xml_file('xml.xml')
