#!/usr/bin/python

print("Content-type: text/html\n")
print("""
<html>
<head>
<title>ChartDirector Ver 5.1 Sample Programs</title>
</head>
<frameset rows="19,*" framespacing="0">
    <frame
        name="indextop"
        src="indextop.py"
        scrolling="no"
        frameborder="1"
    />
    <frameset cols="222,*" framespacing="0">
        <frame
            name="indexleft"
            src="indexleft.py"
            scrolling="auto"
            frameborder="1"
        />
        <frame
            name="indexright"
            src="indexright.py"
            scrolling="auto"
            frameborder="1"
        />
    </frameset>
</frameset>
</html>
""")
