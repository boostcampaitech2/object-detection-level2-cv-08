python train.py --project recycle_trash_OD --name yolov5x6 --img 1024 --batch 4 --save-period 10 --multi-scale --noval --data data/recycle.yaml --weights yolov5x6.pt --device 0
python train.py --project recycle_trash_OD --name yolov5l6 --img 1024 --batch 4 --save-period 10 --multi-scale --noval --data data/recycle.yaml --weights yolov5l6.pt --device 0
python train.py --project recycle_trash_OD --name yolov5m6 --img 1024 --batch 4 --save-period 10 --multi-scale --noval --data data/recycle.yaml --weights yolov5m6.pt --device 0
python train.py --project recycle_trash_OD --name yolov5s6 --img 1024 --batch 4 --save-period 10 --multi-scale --noval --data data/recycle.yaml --weights yolov5s6.pt --device 0

