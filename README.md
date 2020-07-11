# kaggle_timm_pretrained
kaggle_timm_pretrained is a monkey patch for using timm in kaggle. This patch modifies the location of pretrained models to local file system. This means that you can use pretrained models in kaggle GPU kernels.

## How to use
1. Use any data sources in the following table
2. Use the patch functions such as following
```
import timm
from kaggle_timm_pretrained import patch

patch(["../input/timm-pretrained-vovnet/vovnet"])
```
3. Create network with passing pretrained as true as usual

## Support models
|  Network  |  Data sources  |
| ---- | ---- |
|  densenet  | [/ar90ngas/timm-pretrained-densenet](https://www.kaggle.com/ar90ngas/timm-pretrained-densenet)   |
|  dla  |  [ar90ngas/timm-pretrained-dla](https://www.kaggle.com/ar90ngas/timm-pretrained-dla)  |
|  dpn  |  [ar90ngas/timm-pretrained-dpn](https://www.kaggle.com/ar90ngas/timm-pretrained-dpn)  |
|  efficientnet  |  [ar90ngas/timm-pretrained-efficientnet](https://www.kaggle.com/ar90ngas/timm-pretrained-efficientnet)  |
|  hrnet  |  [ar90ngas/timm-pretrained-hrnet](https://www.kaggle.com/ar90ngas/timm-pretrained-hrnet)  |
|  mobilenetv3  |  [ar90ngas/timm-pretrained-mobilenetv3](https://www.kaggle.com/ar90ngas/timm-pretrained-mobilenetv3)  |
|  nasnet  |  [ar90ngas/timm-pretrained-nasnet](https://www.kaggle.com/ar90ngas/timm-pretrained-nasnet)  |
|  pnasnet  |  [ar90ngas/timm-pretrained-pnasnet](https://www.kaggle.com/ar90ngas/timm-pretrained-pnasnet)  |
|  regnet  |  [ar90ngas/timm-pretrained-regnet](https://www.kaggle.com/ar90ngas/timm-pretrained-regnet)  |
|  res2net  |  [ar90ngas/timm-pretrained-res2net](https://www.kaggle.com/ar90ngas/timm-pretrained-res2net)  |
|  resnest  |  [ar90ngas/timm-pretrained-resnest](https://www.kaggle.com/ar90ngas/timm-pretrained-resnest)  |
|  resnet  |  [ar90ngas/timm-pretrained-resnet](https://www.kaggle.com/ar90ngas/timm-pretrained-resnet)  |
|  selecsls  |  [ar90ngas/timm-pretrained-selecsls](https://www.kaggle.com/ar90ngas/timm-pretrained-selecsls)  |
|  senet  |  [ar90ngas/timm-pretrained-senet](https://www.kaggle.com/ar90ngas/timm-pretrained-senet)  |
|  sknet  |  [ar90ngas/timm-pretrained-sknet](https://www.kaggle.com/ar90ngas/timm-pretrained-sknet)  |
|  tresnet  |  [ar90ngas/timm-pretrained-tresnet](https://www.kaggle.com/ar90ngas/timm-pretrained-tresnet)  |
|  vovnet  |  [ar90ngas/timm-pretrained-vovnet](https://www.kaggle.com/ar90ngas/timm-pretrained-vovnet)  |

## Acknowledgments
* [pytorch-image-models](https://github.com/rwightman/pytorch-image-models) 
