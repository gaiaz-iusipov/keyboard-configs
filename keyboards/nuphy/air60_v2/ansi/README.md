## [NuPhy Air60 V2](https://nuphy.com/products/air60-v2)

1. Install [Vitaly](https://github.com/bskaplou/vitaly?tab=readme-ov-file#installation)
2. Connect a keyboard vie USB cable

```shell
python3 patch.py layout.vil > temp.vil
vitaly -i 12885 load -m via.json -f temp.vil
rm temp.vil
```
