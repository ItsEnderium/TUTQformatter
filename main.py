import re
with open("Inputs/Input.txt") as fh:
  text=fh.read()
text=text[text.index("[b]1.1"):]
text=text.replace("\n\n[b]","NEWLINE")
text=text.replace("\n","[p]")
text=text.replace("NEWLINE","\n[b]")
text=text.replace("[p][p]","[/p]‎[p]")
text=text.replace("[scratchblocks][p]","[scratchblocks]")
text=text.replace("[p][/scratchblocks]","[/scratchblocks]")
text=re.sub(r'\[/p\]‎\[p\]\[big\]\[b\]\[u\].*?\[/u\]\[/b\]\[/big\]','',text)
text=re.sub(r'\[/p]‎\[p\]\[big\]\[b\]\[u\]([\s\S]*?)\[/u\]\[/b\]\[/big\]','',text)
text=text.replace("“",'"')
text=text.replace("”",'"')
with open("Outputs/TextOutput.txt", "w") as file:
  file.write(text)
text=re.sub(r'\[url=.*?\]','',text)
text=text.replace("[/url]","")
text=text.replace("[/b]","")
text=text.replace("[b]","")
text=re.sub(rf'{re.escape("[p]")}.+?$', '', text, flags=re.MULTILINE)
text=text.replace("[i][/i]","")
with open("Outputs/TitlesOutput.txt", "w") as file:
  file.write(text)
print("Written")