scores=[65,90,45,80,50,76,88,92,59,30]
result=[]

for score in scores:
    if score >= 60:
       result.append((score,"PASS"))
    else:
        result.append((score,"FAIL"))

for score, status in result: 
    print(f"score:   {score}  ->  {status}")