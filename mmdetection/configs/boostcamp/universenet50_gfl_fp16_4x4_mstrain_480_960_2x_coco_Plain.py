pretrained = 'https://github.com/shinya7y/UniverseNet/releases/download/20.07/universenet50_gfl_fp16_4x4_mstrain_480_960_2x_coco_20200729_epoch_24-c9308e66.pth'  # noqa

_base_ = [
    'models/universenet50_gfl.py',
    'config/dataset_mstrain_480_960.py',
    'config/default_runtime.py',
    'config/schedule.py'
]

data = dict(samples_per_gpu=4)

optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(
    _delete_=True, grad_clip=dict(max_norm=35, norm_type=2))

lr_config = dict(
    _delete_=True,
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[16, 22])
runner = dict(type='EpochBasedRunner', max_epochs=24)

fp16 = dict(loss_scale=512.)

log_config = dict(
    _delete_=True,
    interval=50,
    hooks=[
        dict(type="TextLoggerHook"),
        dict(type="WandbLoggerHook", init_kwargs=dict(project="recycle_trash_OD", name="universenet50_gfl_fp16_4x4_mstrain_480_960_2x_coco_Plain")),
    ],
)