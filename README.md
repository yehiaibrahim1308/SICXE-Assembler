# SICXE-Assembler
This SIC/XE assembler code project is designed to read and process assembly language instructions and corresponding tables from specified text files. The primary objective of the project is to generate object code that adheres to the SIC/XE format, utilizing the provided instructions and symbol tables.
                  
                          
# Components 
## Input Files:
  
### Instructions File:
- Contains the assembly language source code in SIC/XE format, including header (H), text (t), and end (E) records. Each instruction line specifies operation codes, addresses, and data in a structured format.
- Table File: Includes the symbol table and literal table, providing addresses and object codes for the various operations defined in the instruction file. This file is crucial for resolving symbolic references and generating accurate object code.

### Parsing and Processing:
 
- Table Parsing: The assembler extracts addresses and object codes from the table file. This information is used to correlate symbolic references with their respective machine codes and addresses.
- Instruction Parsing: The assembler reads and processes instructions from the instructions file. It decodes the header record, text records, and end record, handling symbolic references and converting them into machine-readable formats.

# Object Code Generation:

- Header Record (H): Defines the program name, starting address, and length of the object code. This record is essential for linking and loading the program.
- Text Records (t): Contains the actual machine code for each segment of the program. Each text record includes the starting address, length of the code, and the object code itself.
- End Record (E): Specifies the starting address of the program's execution. This record marks the end of the object code and facilitates correct program execution.
