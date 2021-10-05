#python tools/train.py configs/boostcamp/mask_rcnn_hrnetv2_w32.py
#python tools/train.py configs/boostcamp/mask_rcnn_r50.py
#python tools/train.py configs/boostcamp/
#python tools/train.py configs/boostcamp/
#python tools/train.py configs/boostcamp/

./tools/dist_train.sh configs/boostcamp/universenet101_gfl_fp16_4x4_mstrain_480_960_2x_coco.py 2
./tools/dist_train.sh configs/boostcamp/universenet101_gfl_fp32_4x4_mstrain_480_960_2x_coco.py 2

