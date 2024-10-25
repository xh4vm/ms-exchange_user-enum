# MS Exchange User Enumeration

## Introduction
A user enumeration vulnerability was discovered in the MS Exchange Server 2019/2016 application. This method was tested on MS Exchange Server 2019 CU 14 (build: 15.02.1544.011) and MS Exchange Server 2016 CU 23 (build: 15.01.2507.039).

Microsoft closed the report without using the CVE identifier , but in my opinion, this is indeed a vulnerability.

## Demonstation

## Use code
```
git clone https://github.com/xh4vm/ms-exchange_user-enum
cd ./ms-exchange_user-enum
poetry install
poetry run python3 main.py -t <host or file> -u <user or file>
```

## Reference
