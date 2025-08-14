from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend

with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

def encrypt(text):
    text = text.encode("utf-8")
    ciphertext = public_key.encrypt(
        text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def unencrypt(text):
    decrypted_text = private_key.decrypt(
        text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_text


plain = unencrypt(b"\x003\x93p\xb1\xa0\x9f\xb1`\xac7\xf6\xb6\xe2\t#V\xb2i\xe1\x1a\x94\xea\xabt(.\xec\x8e7\xe0\xa6\xd5\xe6\x82Sw\xfd\xb2N\xa3`J\xe37Yc\xd4:\xee\xef(b\xdb\xdc\xe0\xfeL\x809\x7f\x1c\x9cv\xcf,'\xfa\xc4\x81Sy<\xf9S[mo'\xcb\xd2\x0cd$kj\xe6\xd4\x12S\x1em^\x0c\xff\x98mi\xcd\xc7\xbb\xac$\xe1\xc0\xbd\xe6\xceN\xd8\x9e\x96\xe4U`rM\xb4\xedC2\x1f\xee\xa3~?\x9c$\xb8\xa1\x0c\x00\xca\xf3\x05\x99\x19\xef\xe4\xe8\x9bp\x8f\x14\xfa*\xac\xde\x05\xeb\xe5+C\xffg\xcc\x8f\xac\x89\r,\x19\x97Vi\xdb2\x85{\x8dL\xa4\xbf?k\xec\xafu\x15\x97\xb1\x9c\xbe}\xf6\x90\xcf\x81]\xdc\x915\xd5\xe2M_\xa7m\xa8\x94\x82{\xfa\x14>I\t\xe2\xc4\x98\xc6/\xef\xba\xfeM\x12\x90r\x88\x0bjf\x89\x97\xa7\x1c\xe7\xc5\xf6\x08\xc9\xc5t\x85\xd9~\xd6_w\x05\xf4\xce\x81\xe23\xccZ\xa4\x12\xda\xaa\xb7I\xc9\x06"
).decode("utf-8")  # обратно в строку
print(plain)
