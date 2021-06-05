with open("Packages", 'r') as f:
        data = f.read()
data = data.replace('Version: 1.1.1d-0+deb10u3','Version: 1.1.1i-1')

data = data.replace('Filename: pool/main/o/openssl/libssl-dev_1.1.1d-0+deb10u3_amd64.deb','Filename: pool/main/o/openssl/libssl-dev_1.1.1i-1_amd64.deb')
data = data.replace('SHA256: a37897b52338012c3864a76533f536ff9e2b2c6e353fb01ef90b13c3976a788b','SHA256: fb488c918b8c2d1ccba3e67c09c6265e749bf1f86c585391c2801422dcb99dd5')

data = data.replace('Filename: pool/main/o/openssl/libssl-doc_1.1.1d-0+deb10u3_all.deb','Filename: pool/main/o/openssl/libssl-doc_1.1.1i-1_all.deb')
data = data.replace('SHA256: 88969f5a59bb04afda4f06ee2b3558f4f90eaee657a0951b6d52c7c647931054','SHA256: 6f56a71b2dcbdc9c96fd06c0b78f8a4ed32e6d0ea29f2abf6d4c72af4294a96c')

data = data.replace('Filename: pool/main/o/openssl/libssl1.1_1.1.1d-0+deb10u3_amd64.deb','Filename: pool/main/o/openssl/libssl1.1_1.1.1i-1_amd64.deb')
data = data.replace('SHA256: b293309a892730986e779aea48e97ea94cd58f34f07fefbd432c210ee4a427e2','SHA256: c7f9a2e6153a6a7912d11747352391cc6ed410f447a38abfb345c287f6e31cc0')

data = data.replace('Filename: pool/main/o/openssl/openssl_1.1.1d-0+deb10u3_amd64.deb','Filename: pool/main/o/openssl/openssl_1.1.1i-1_amd64.deb')
data = data.replace('SHA256: 03a133833154325c731291c8a87daef5962dcfb75dee7cdb11f7fb923de2db82','SHA256: 9c82849c256bf2bc3abe7d6f301f3e17a5738f34a5023688a08b289b90b98156')

with open("new_package", 'w') as f:
        f.write(data)