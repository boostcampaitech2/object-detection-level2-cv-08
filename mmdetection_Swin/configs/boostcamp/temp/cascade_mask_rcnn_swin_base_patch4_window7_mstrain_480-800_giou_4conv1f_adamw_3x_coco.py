_base_ = [
    '/opt/ml/detection2/UniverseNet/configs/boostcamp/models/cascade_rcnn_swin_fpn.py',
    '/opt/ml/detection2/UniverseNet/configs/boostcamp/config/dataset_multiscale.py',
    '/opt/ml/detection2/UniverseNet/configs/boostcamp/config/default_runtime.py',
    '/opt/ml/detection2/UniverseNet/configs/boostcamp/config/schedule_JH_Custom.py',
]

pretrained = 'https://download.openmmlab.com/mmclassification/v0/swin-transformer/swin_small_224_b16x64_300e_imagenet_20210615_110219-7f9d988b.pth'

model = dict(
    backbone=dict(
        embed_dim=128,
        depths=[2, 2, 18, 2],
        num_heads=[4, 8, 16, 32],
        window_size=7,
        ape=False,
        drop_path_rate=0.3,
        patch_norm=True,
        use_checkpoint=False),
    neck=dict(in_channels=[128, 256, 512, 1024]),)
    
optimizer = dict(
    _delete_=True,
    type='AdamW',
    lr=0.0001,
    betas=(0.9, 0.999),
    weight_decay=0.05,
    paramwise_cfg=dict(
        custom_keys={
            'absolute_pos_embed': dict(decay_mult=0.),
            'relative_position_bias_table': dict(decay_mult=0.),
            'norm': dict(decay_mult=0.)
        }))
# fp16 = dict(loss_scale=512.)
lr_config = dict(warmup_iters=1000, step=[27, 33])
runner = dict(max_epochs=36) # 12->30->36->40
log_config = dict(
    _delete_=True,
    interval=50,
    hooks=[
        dict(type="TextLoggerHook"),
        dict(type="WandbLoggerHook", init_kwargs=dict(project="recycle_trash_OD", name="cascade_mask_rcnn_swin_base_patch4_window7_mstrain_480-800_giou_4conv1f_adamw_3x_coco")),
    ],
)
