import pickle
file=open('temp.txt',"a+")
data={
    'fullname':"kanika Goyal",
    'userid':"22BCON701",
    'password':"***",
    
}
enc_data=pickle.dumps(data)
file.write(enc_data)
file.seek(0)
enc_data=file.read()
print(type(enc_data))
ori_data=pickle.loads(enc_data)
print(ori_data,type(ori_data))