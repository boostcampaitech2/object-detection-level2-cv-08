_base_ = [
    '/opt/ml/detection2/UniverseNet/configs/boostcamp/models/cascade_rcnn_r50.py',
    '/opt/ml/detection2/UniverseNet/configs/boostcamp/config/dataset_multiscale_mosaic.py',
    '/opt/ml/detection2/UniverseNet/configs/boostcamp/config/default_runtime.py',
    '/opt/ml/detection2/UniverseNet/configs/boostcamp/config/schedule_JH_Custom.py',
]

pretrained = 'https://download.openmmlab.com/mmclassification/v0/swin-transformer/swin_small_224_b16x64_300e_imagenet_20210615_110219-7f9d988b.pth'
model = dict(
    backbone=dict(
        _delete_=True,
        type='SwinTransformer',
        embed_dims=96,
        depths=[2, 2, 18, 2], # 6->18
        num_heads=[3, 6, 12, 24],
        window_size=7,
        mlp_ratio=4,
        qkv_bias=True,
        qk_scale=None,
        drop_rate=0.,
        attn_drop_rate=0.,
        drop_path_rate=0.2,
        patch_norm=True,
        out_indices=(0, 1, 2, 3),
        with_cp=False,
        convert_weights=True,
        init_cfg=dict(type='Pretrained', checkpoint=pretrained)),
    neck=dict(in_channels=[96, 192, 384, 768]))

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
runner = dict(max_epochs=45) # 12->30->36->40
log_config = dict(
    _delete_=True,
    interval=50,
    hooks=[
        dict(type="TextLoggerHook"),
        dict(type="WandbLoggerHook", init_kwargs=dict(project="recycle_trash_OD", name="cascade_rcnn_swin-t-p4-w7_fpn_1x_coco")),
    ],
)
