# diary.txt
# UTF-8 encoding
# [date]sentence\r\n

# open output file
file_out = open("diary.html", mode="w", encoding="utf-8")

# white html before table
file_out.write("""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>diary</title>
</head>
<body>
<table>
""")

# open input file
file_in = open("diary.txt", mode="r", encoding="utf-8")

# read 1 line
line_in = file_in.readline().rstrip()

# begin while
while line_in != "":

    # manipulate strings
    # in:  [date]sentence\r\n
    # out: <tr><td>date</td><td>sentence</td></tr>\r\n
    row = line_in.strip("[]").split("]")
    line_out = "<tr><td>{0[0]}</td><td>{0[1]}</td></tr>\n".format(row)

    # write 1 line
    file_out.write(line_out)

    # read 1 line
    line_in = file_in.readline().rstrip()

# end while

# close input file
file_in.close()

# write html after table
file_out.write("""</table>
</body>
</html>
""")

# close output file
file_out.close()
