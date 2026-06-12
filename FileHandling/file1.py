with open("FileHandling/data.txt","r") as file:
    data = file.read()
print(data)


# 'r'     Open for reading (default)
# 'w'     Open for writing, truncating the file first
# 'x'     Create a new file and open it for writing
# 'a'     Open for writing, appending to the end of the file if it exist
# 'b'     Binary Mode 
# 't'     Text mode 
# '+'     Open a disk file for updating (reading and writing)

#     'r+'    read + overwrite (pointer - start) -- No truncate
#     'w+'    read + overwrite   -- Turncate
#     'a+'    read + append (pointer - end) -- No truncate