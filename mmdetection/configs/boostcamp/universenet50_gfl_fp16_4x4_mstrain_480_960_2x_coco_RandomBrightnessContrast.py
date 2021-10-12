pretrained = 'https://github.com/shinya7y/UniverseNet/releases/download/20.07/universenet50_gfl_fp16_4x4_mstrain_480_960_2x_coco_20200729_epoch_24-c9308e66.pth'  # noqa

_base_ = [
    'models/universenet50_gfl.py',
    'config/dataset_mstrain_480_960_RandomBrightness.py',
    'config/default_runtime.py',
    'config/schedule_adam.py'
]
model = dict(
        init_cfg=dict(type='Pretrained', checkpoint=pretrained),
)
fp16 = dict(loss_scale=512.)
log_config = dict(
    _delete_=True,
    interval=50,
    hooks=[
        dict(type="TextLoggerHook"),
        dict(type="WandbLoggerHook", init_kwargs=dict(project="recycle_trash_OD", name="universenet50_gfl_fp16_4x4_mstrain_480_960_2x_coco_RandomBrightnessContrast_adam")),
    ],
)