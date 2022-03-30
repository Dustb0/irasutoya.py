# irasutoya.py
Get images from irasutoya.com with search terms in Japanese. English is currently not supported. Web scraping is used to retrieve the images.

![alt text](/readme.png)

## Dependencies
Install dependencies with pip using the requirements.txt:
```
pip install -r requirements.txt
```

## Usage

```python
from irasutoya import Irasutoya

Irasutoya.get_image('自分')

# returns 
# ['https://3.bp.blogspot.com/-Zd4xn4GcDoc/Wb8gV2l2wmI/AAAAAAABGxA/Dir3I4uSGg8BHsAxCCNf--GovRMNg0J5ACLcBGAs/s180-c/inu_shippo_oikakeru.png', 'https://3.bp.blogspot.com/-9zuN2OZXocg/WR_Kx4Fan5I/AAAAAAABEZs/dCNfy21rizINz_njdXE5bek8cCjGWKVSQCLcB/s180-c/jibun_sagashi_man.png', ... ]
```