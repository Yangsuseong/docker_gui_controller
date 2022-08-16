* 사진이 첨부된 메뉴얼은 manual.pdf 파일 참고

# Docker GUI Controller
* Requirements
	* python3-tk Package
	* Docker
	* Ubuntu OS

::tkinter install::
```bash
$ sudo apt install python3-tk
```


## Admin용 GUI Controller
---

### 실행 방법
```bash
$ python ./docker_gui_controller/admin/run.py 
```

[image:69E19AE1-E507-4FC6-9FBC-9D2CA6D63CCB-23049-00000159F2FC1760/스크린샷 2022-08-16 오전 11.47.11.png]

### Image 관리

#### Docker pull
::Images 탭 에서 Pull 버튼 클릭::
[image:01682EBA-1C45-479F-970B-4646342D586D-23049-0000015DAF044F3E/0B84BF5D-D16A-4A16-BBC2-3E8E5DFC17B3.png]

::받아올 이미지 이름과 Tag를 입력 후 Summit 버튼 클릭::
[image:8B9033B7-7715-49DD-BCB1-34D6B46E97B3-23049-0000015DD962C4CF/A3F5D06F-63E5-4F2C-B53D-3715778849FB.png]

::터미널에서 이미지 Pull 진행 확인::
[image:7A5989AA-74F6-4C40-BE25-10F72D5706DB-23049-0000015E48AD8FB0/0335231F-2C59-49F6-8E62-D7F180A4AE84.png]

::Pull 완료된 이미지 확인::
[image:EA299221-8489-4C90-834C-A13E83AC7A9F-23049-0000015E963D183E/0E247763-135C-464C-991A-2A6160502CA2.png]



#### Docker tag
::Images 탭 에서 원하는 이미지 Select 한 이후 Tag 버튼 클릭::
[image:DBD7970B-89E5-4AD4-B585-41B2DBEF1C70-23049-0000015F3AB75630/222452BE-EDF6-43FB-A903-276B9716DCFE.png]

::생성할 이미지 이름과 Tag 를 입력 후 Summit 버튼 클릭::
[image:2E3D095B-0D02-47CF-ABD5-CC60DA95DE86-23049-00000171F250FB4E/스크린샷 2022-08-16 오후 12.58.44.png]
[image:ED73ACB2-CE26-4AB0-B4FF-73385273C338-23049-0000015B1AE2711C/스크린샷 2022-08-16 오전 11.50.38.png]

::이미지 생성 확인::
[image:03DDC7CA-C896-4A4E-BE94-F120BDEC3BCC-23049-000001720CF8D43D/스크린샷 2022-08-16 오후 12.59.03.png]




#### 이미지 Push
::Images 탭 에서 원하는 이미지 Select 한 이후 Push 버튼 클릭::
[image:A470E817-FC5A-424D-A6B3-B5A4FD4EC53D-23049-0000017937A6AEFE/DEA58421-BEC1-483F-AE6C-01FAA20D56A7.png]
[image:8E13DE06-F40D-4578-83C0-10478B6FB2F2-23049-00000160E70E8A66/619E4778-00AE-4E04-94FC-E3A67015CAE7.png]
[image:861A6A03-0562-474E-B921-CF0C0C3E45AA-23049-000001791EEC99B2/스크린샷 2022-08-16 오후 2.00.00.png]

::이미지 업로드 확인::
[image:ADAA4A22-73D2-4304-BF10-54F9CD25E2DD-23049-00000179C89D9852/617B36B7-20ED-4B17-AEC8-7CF95B40567D.png]



#### 이미지 Remove
::Images 탭 에서 원하는 이미지 Select 한 이후 Remove 버튼 클릭::
[image:49F77541-6BC4-48E4-A8E5-F2054A6E7D21-23049-0000017A13E434BA/08591D71-5483-4F70-B76B-68E677169D46.png]
[image:E6999986-462D-4939-BAD8-30E2BC4038F2-23049-0000017A3EDD018C/스크린샷 2022-08-16 오후 2.03.50.png]

::이미지 삭제 확인::
[image:943A2C3B-F24A-4EAF-A921-09FDF0D31783-23049-0000017A5CA6A7A4/2194EC0F-E446-4390-B57B-C1C0D0729A97.png]




### Container 관리

::예시를 위한 컨테이너 생성::
```bash
$ docker run -d --name gui-test ubuntu:20.04
```

::컨테이너 확인::
[image:862A8375-D41C-4B35-990C-78F271B3D74F-23049-0000017BA1429DC7/6B14DF42-526C-4545-B150-251E1EA77493.png]


#### 컨테이너 Start
::Containers 탭 에서 원하는 컨테이너 Select 한 이후 Start 버튼 클릭::
[image:1C843E64-2809-4D54-BE0D-7FA6949D3E7F-23049-0000017C32ACFE6A/E66DE98B-ED94-4C3A-8C07-7E6316757E32.png]
[image:F80E5FB0-E8EF-4BED-8015-AC347B2F352B-23049-0000017C44C0C38E/스크린샷 2022-08-16 오후 2.09.53.png]

::컨테이너 Status 확인::
[image:D7A21041-A478-4CB7-8BE1-C7053F92999F-23049-0000017C93B97D5B/594D6DD0-4874-4D11-90B8-346070CDF791.png]



#### 컨테이너 Stop
::Containers 탭 에서 원하는 컨테이너 Select 한 이후 Stop 버튼 클릭::
[image:C4F73ABA-A47E-40E3-A2CD-7AF45DFFD250-23049-0000017CD945E7BF/스크린샷 2022-08-16 오후 2.11.37.png]
[image:C45320A7-4896-4870-8EBF-972F94DAFF44-23049-0000017CEB5EDBA8/스크린샷 2022-08-16 오후 2.11.49.png]

::컨테이너 Status 확인::
[image:1C994B1B-A49B-44A3-B608-10CA5E5E82F7-23049-0000017D2A960738/23194930-B40A-4A1E-8608-24AA2513BE25.png]



#### 컨테이너 Commit
::Containers 탭 에서 원하는 컨테이너 Select 한 이후 Commit 버튼 클릭::
[image:8F8C32B6-B1B7-4270-BEA0-ECB3CDA51AFC-23049-0000017D69D6EE52/BE8179E9-8879-4601-ABC1-B2B7D6A81450.png]

::커밋할 이미지 이름과 태그 입력 후 Summit 버튼 클릭::
[image:FCC08BC4-5870-42D2-B1E4-EFEF73AD63C3-23049-0000017DB4E3BB71/스크린샷 2022-08-16 오후 2.14.09.png]
[image:9C216CB1-217B-4AA5-A502-4F6B6992D462-23049-0000017E2E38CF48/스크린샷 2022-08-16 오후 2.15.34.png]

::Images 탭에서 커밋한 이미지 확인::
[image:68268897-FC85-465F-B0FB-42D64F3039D9-23049-0000017E60B363C1/1091FD16-307E-4948-87AD-FB06FEBB4ED3.png]



#### 컨테이너 삭제
::Containers 탭 에서 원하는 컨테이너 Select 한 이후 Remove 버튼 클릭::
[image:68813EE5-0F6C-440A-8FDB-42C5B296E159-23049-0000017EEB7EB2FB/073F44B1-9D87-4357-B38A-09A79DF291A5.png]

::확인 단계에서 Summit 버튼 클릭::
[image:617BE053-70A8-4869-94E6-29847544EBE8-23049-0000017F09843279/ECC71B02-A61A-441B-ACFF-C48A8F50064A.png]

::컨테이너 삭제 확인::
[image:93344796-CD52-4A7C-8BEF-C349BDB4B2D5-23049-0000017F3DAB6675/5FEAB16D-30B0-49C4-A5E6-20A454E4D599.png]








## User 용 GUI Controller
---

### 실행 방법
```bash
$ python3 ./docker_gui_controller/Common_user/run.py
```

### 실행 예시
[image:82AF2992-6CE6-41A7-9959-A6F2DA0D7941-23049-00000189F24DC6AC/스크린샷 2022-08-16 오후 2.50.41.png]

::Docker images::
* 사용할 이미지를 선택하여 Select 버튼 클릭

::—rm Option::
* 컨테이너에 --rm 옵션을 사용할 시 체크박스 체크

::GPU Count::
* 컨테이너에 사용할 GPU의 개수를 선택
* 자동으로 사용 가능한 최대 개수를 제한함
* CPU 만 사용할 경우 GPU Count를 0으로 선택

::Container Name::
* 컨테이너의 이름을 지정
* 코드 실행 시 계정명+Index 로 자동으로 이름이 겹치지 않게 지정됨

::Mount Option::
* 컨테이너에 디스크를 마운트 할 경우 체크박스 체크
* 로컬 디렉토리 경로와 컨테이너 디렉토리 경로를 입력하여 마운트

::Port Fowarding Option::
* 컨테이너에 포트포워딩을 할 경우 체크박스 체크
* 로컬 포트와 컨테이너 포트를 입력하여 포트포워딩

::Command::
* 컨테이너 실행 시 실행할 Command를 입력



### 실행 결과
[image:BC5DAE02-0D6E-4D3A-9393-55EBF26DDA6D-23049-0000018A0D535984/스크린샷 2022-08-16 오후 2.50.59.png]

#### Mount 동작 확인
::컨테이너에서 마운트 포인트에 aaa.txt 파일 생성::
```bash
root@88d837e35a07:/# cd /mount_test && touch aaa.txt
root@88d837e35a07:/mount_test# ls
>>> aaa.txt  mw_ost_tools  yss-kubeconfig
```

::로컬 마운트 포인트에 파일 생성 확인::
```bash
$ ls /home/yss
>>> aaa.txt  mw_ost_tools  yss-kubeconfig
```









## Trouble Shooting
---

### Docker 권한이 없는 경우
```bash 
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/images/json": dial unix /var/run/docker.sock: connect: permission denied
```

Tool 을 사용하는 계정을 Docker 그룹에 추가하여 해결

```bash
$ sudo usermod -aG docker $USER
```


### Nvidia driver 가 없는 경우
```bash
sh: 1: nvidia-smi: not found
```

GPU 서버가 아닌 경우 무시해도 상관 없고
GPU 서버인 경우 NVIDIA Driver 를 설치하여 해결
