pretrained = 'https://github.com/shinya7y/UniverseNet/releases/download/20.07/universenet101_gfl_fp16_4x4_mstrain_480_960_2x_coco_20200716_epoch_24-1b9a1241.pth'  # noqa

_base_ = [
    'models/universenet101_gfl.py',
    'config/dataset_mstrain_480_960.py',
    'config/default_runtime.py',
    'config/schedule_JH_Custom.py'
]
model = dict(
        init_cfg=dict(type='Pretrained', checkpoint=pretrained),
)


data = dict(samples_per_gpu=16)

# optimizer = dict(type='Adam', lr=0.0001, weight_decay=0.0001)
# optimizer_config = dict(
#     _delete_=True, grad_clip=dict(max_norm=35, norm_type=2))
# lr_config = dict(warmup_iters=1000)

fp16 = dict(loss_scale=512.)

# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[16, 22])
runner = dict(type='EpochBasedRunner', max_epochs=30)

log_config = dict(
    _delete_=True,
    interval=50,
    hooks=[
        dict(type="TextLoggerHook"),
        dict(type="WandbLoggerHook", init_kwargs=dict(project="recycle_trash_OD", name="universenet101_gfl_fp16_4x4_mstrain_480_960_2x_coco_mixup_batch16")),
    ],
)
