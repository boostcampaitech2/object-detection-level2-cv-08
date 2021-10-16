# pstage_02_Object_Detection

## Getting Started    
## Dependencies
```
# MMDetection setting
conda create -n mmdet python=3.7 -y

conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.1 -c pytorch -y

pip install openmim

mim install mmdet


# YOLOv5 setting
conda create -n yolov5 python=3.8 -y

conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.1 -c pytorch -y

cd yolov5

pip install -r requirements.txt

python example.py --datasets COCO --img_path ../dataset/train/ --label ../dataset/train.json --convert_output_path ../dataset/ --img_type ".jpg" --manifest_path ./ --cls_list_file recycle.names
```

__Install Requirements__

`pip install -r requirements.txt`



## Train

### YOLO v5

```bash
cd yolov5-master
python train.py --ms
```

### PVT v2

```python
cd /mmdetection_PVT
# pip install -v -e . 실행
python tools/train.py configs/boostcamp_trash_PVTv2_b3_custom/final.py

```

### UniverseNet-101
```python
cd/mmdetection
python tools/train.py configs/boostcamp/universenet101_gfl_fp16_4x4_mstrain_480_960_2x_coco.py 
```

### Swin

```python
cd /mmdetection_Swin 

# pip install -v -e . <- 실행

python tools/train.py configs/boostcamp/temp/cascade_rcnn_swin-s-p4-w7_fpn_ms-crop-3x_coco.py
```


## Ensemble
```python
python ensemble.py ensemble.json
```



