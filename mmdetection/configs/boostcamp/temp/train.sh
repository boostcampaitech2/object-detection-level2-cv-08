#python tools/train.py configs/boostcamp/mask_rcnn_hrnetv2_w32.py
#python tools/train.py configs/boostcamp/mask_rcnn_r50.py
#python tools/train.py configs/boostcamp/
#python tools/train.py configs/boostcamp/
#python tools/train.py configs/boostcamp/

./tools/dist_train.sh configs/boostcamp/cascade_rcnn_swin-s-p4-w7_fpn_fp16_ms-crop-3x_coco.py 2
./tools/dist_train.sh configs/boostcamp/cascade_rcnn_swin-t-p4-w7_fpn_ms-crop-3x_coco.py 2

