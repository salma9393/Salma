#formatted string-2
text="python"
print(f"i am learning {text}{{}}")
print(f"i am learning {{{text}}} {{}}")


print(f"[{text:>20}]")
print(f"[{text:<20}]")
print(f"[{text:^20}]")

stats=["cricketer","runs","balls"]
p1=["rohi",30,20]
p2=["raji",10,15]
p3=["rockey",15,60]
print(f"{stats[0]:>15}{stats[1]:>15}{stats[2]:^15}")
print(f"{p1[0]:>15}{p1[1]:>15}{p1[2]:^15}")
print(f"{p2[0]:>15}{p2[1]:>15}{p2[2]:^15}")
print(f"{p3[0]:>15}{p3[1]:>15}{p3[2]:^15}")



s1="python"
s2="java"
s3="c language"
languages=f"first={s1},second={s2},third={s3}"
print(languages)


