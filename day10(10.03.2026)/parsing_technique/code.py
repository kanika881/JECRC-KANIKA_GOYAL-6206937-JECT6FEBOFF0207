##dumps():Encryption 
##loads():Decryption
'''
1. JSON
2. pickle
'''
import json 
file=open('temp.txt',"a+")
data={
    'fullname':"kanika Goyal",
    'userid':"22BCON701",
    'password':"***",
    
}

# print(f"original data: {data}")
# print(f"Type of original data : {type(data)}")

enc_data=json.dumps(data)
file.write(enc_data)
file.seek(0)
enc_data=file.read()
print(type(enc_data))
ori_data=json.loads(enc_data)
print(ori_data,type(ori_data))
# print("Encrypted data:",enc_data)
# print(f"Type of encrypted data: {type(enc_data)}")
# dec_data=json.loads(enc_data)
# print("Dencrypted data:",dec_data)
# print(f"Type of Dencrypted data: {type(dec_data)}")

