line="PPTPPTPTP"
police_count=0;
theif_count=0;
police_seen=False;
for person in line:
    if person=="P":
        # police_count+=1
        police_seen=True

    elif person=="T" and police_seen:
        theif_count+=1
        police_seen=False

print(f"theif={theif_count}")