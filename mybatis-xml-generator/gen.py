
# Input sample.txt which save table headers
# Output insert, update, and so on
 
file = open("headers.txt")
ins = open("insert.txt", "w")
upd = open("update.txt", "w")
 
while 1:
    line = file.readline()
    line=line.strip('\n')
    if not line:
        break
    upd.write(line + " = #{" + line + "},")
    upd.write("\n")
    ins.write("#{" + line + "}")
    ins.write("\n")
    
