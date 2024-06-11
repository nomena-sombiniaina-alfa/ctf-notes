with open('passwd.txt', 'w') as f1, open('step.txt', 'w') as f2:
    for i in range(1,34):
        f1.write(f"key {i} :\n\tusername : century{i}\n\tpassword : \n")
        f2.write(f"step {i} : \n")