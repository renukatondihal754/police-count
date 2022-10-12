line="PPTPPTPTP"
police_count=0;theif_count=0
for person in line:
    if person=="P":
        police_count+=1

    elif person=="T":
        theif_count+=1

print(f"police={police_count} ,theif={theif_count}")