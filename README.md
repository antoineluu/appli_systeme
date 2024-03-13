# Autofocus SAR project code

This repository and the data was taken and adapted from this [project](https://github.com/aisari/AutofocusSAR)

```bib
@article{Liu2021Fast,
  title={Fast SAR Autofocus Based on Ensemble Convolutional Extreme Learning Machine},
  author={Liu, Zhi and Yang, Shuyuan and Feng, Zhixi and Gao, Quanwei and Wang, Min},
  journal={Remote Sensing},
  volume={13},
  number={14},
  pages={2683},
  year={2021},
  publisher={Multidisciplinary Digital Publishing Institute},
  doi={https://doi.org/10.3390/rs13142683}
}
```


# Prepare
Python version: 3.9.9
Please update the value of ``SAR_AF_DATA_PATH`` in 'data.yaml' to your dataset path.
You should also 
Do pip ``pip install -r requirements.txt``

# Download


## Model
(``RealPE.tar.bz2``) on ALOS PALSAR dataset from [Google Drive](https://drive.google.com/drive/folders/1aAIdmY-pYGH3PCuHVTf43Wh0Hcg7mzIb?usp=sharing). Put it here and uncompress it.
64CELMs model trained by the authors [doi](https://doi.org/10.3390/rs13142683)
The models we trained is [32CELMs](/snapshot/BaggingECELMs/RealPE/2021/weights/32CELMs.pth.tar) and [8CELMs](/snapshot/BaggingECELMs/RealPE/2021/weights/8CELMs.pth.tar)
## Data: 
Image patches with size 256×256:[Part 1](https://mega.nz/folder/02khBbbb#eeWwsYAGVXVpSah9wn5lUQ) [Part 2](https://mega.nz/folder/DY8EzDya#BH3z6N7dEzL05C5OF8xlMw)
(More than 15 Gb)


# Training

```
python train.py
Configure the right model in ecelm.yaml
```

# Testing

```
python test.py
Select the right .pth filename to use the model you want, then execute.
```

