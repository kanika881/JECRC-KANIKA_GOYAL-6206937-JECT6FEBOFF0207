file=open("jecrc.txt","a+")

# file.write("JECRC is the wolrd's best university!")
# file.write("JECRC is popular for its placement")
# file.writelines([
#     '\n Here food is good',
#     '\nECO system is good',
#     '\n Faculties are supportive',
# ])
file.seek(0)
print(file.read())
file.close()