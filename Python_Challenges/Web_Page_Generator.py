import webbrowser

f = open("summersale.html" , "w")
f.write("<html>\n\t<body>\n\t\t<h1>\n\t\t\tStay tuned for our amazing summer sale!\
\n\t\t</h1>\n\t</body>\n</html>")
f.close()

webbrowser.open_new_tab('summerrsale.html')
        
