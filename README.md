# Microsoft Exchange Server - User Enumeration

## Introduction
A user enumeration vulnerability was discovered in the MS Exchange Server 2019/2016 application. This method was tested on MS Exchange Server 2019 CU 14 (build: 15.02.1544.011) and MS Exchange Server 2016 CU 23 (build: 15.01.2507.039).

## Demonstation


https://github.com/user-attachments/assets/61253d2f-f8e0-4116-a95d-34ef06f17e0a



## Use code
```
git clone https://github.com/xh4vm/ms-exchange_user-enum
cd ./ms-exchange_user-enum
poetry install
poetry run python3 main.py -t <host or file> -u <user or file>
```

## Reference
- [BDU:2024-08516](https://bdu.fstec.ru/vul/2024-08516)
