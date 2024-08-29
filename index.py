import sys

if len(sys.argv) < 2:
    print("No question provided: program terminated")
    sys.exit(1)

question = sys.argv[1].lower()

if question == "/name":
    print("My name is Cayden and I am a Junior this semester!")
elif question == "/why":
    print("I chose CS because my dad also has a CS degree. It is familiar to me, and I enjoy figuring out how computers work. I've enjoyed messing with computers from a very young age.")
elif question == "/what":
    print("I am not positive exactly what I want to do with my degree, but I would like a job that has some sort of graphic element as I enjoy the visual aspect of coding as well as the background programs. I also may pursue a GIS minor as i'm one course away from that in addition to my degree")
elif question == "/fact":
    print("I'm a junior in college and I'm only 17!")    
else:
    print("Invalid response: program terminated")
