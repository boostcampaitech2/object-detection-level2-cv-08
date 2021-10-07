# pstage_02_Object_Detection

## Getting Started    
### Dependencies

[comment]: <> (- pytorch==1.9.0)

[comment]: <> (- pytorch-lightning==1.4.4)

[comment]: <> (- pandas==1.1.5)

[comment]: <> (- opencv-python==4.5.1.48)

[comment]: <> (- scikit-learn~=0.24.1)

[comment]: <> (- matplotlib==3.2.1)

- conda create -n mmdet python=3.7 -y
- conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.1 -c pytorch -y
- pip install openmim
- mim install mmdet

- conda create -n yolov5 python=3.8 -y
- conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.1 -c pytorch -y
- cd yolov5 
- pip install -r requirements.txt

- python example.py --datasets COCO --img_path ../dataset/train/ --label ../dataset/train.json --convert_output_path ../dataset/ --img_type ".jpg" --manifest_path ./ --cls_list_file recycle.names
### Install Requirements
- `pip install -r requirements.txt`

