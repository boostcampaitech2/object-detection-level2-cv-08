_base_ = [
    'models/vfnet_x101_64x4d_fpn_mdconv_c3-c5_mstrain.py',
    'config/dataset.py',
    'config/default_runtime.py',
    'config/schedule.py'
]


optimizer = dict(type="SGD", lr=0.001, momentum=0.9, weight_decay=0.0001, paramwise_cfg=dict(bias_lr_mult=2.0, bias_decay_mult=0.0))
optimizer_config = dict(grad_clip=None)
lr_config = dict(policy="step", warmup="linear", warmup_iters=500, warmup_ratio=0.1, step=[16, 22])
runner = dict(type="EpochBasedRunner", max_epochs=24)
checkpoint_config = dict(interval=1, max_keep_ckpts=5)

log_config = dict(
    _delete_=True,
    interval=50,
    hooks=[
        dict(type="TextLoggerHook"),
        dict(type="WandbLoggerHook", init_kwargs=dict(project="recycle-object_detection", name="vfnet_x101_64x4d_fpn_mdconv_c3-c5_mstrain")),
    ],
)