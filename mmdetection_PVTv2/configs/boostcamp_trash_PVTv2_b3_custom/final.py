_base_ = [
    'cascade_rcnn_r50_fpn.py',
    'dataset.py',
    'default_runtime.py',
    'schedule_1x.py'
]
model = dict(
    backbone=dict(
        _delete_=True,
        type='PyramidVisionTransformerV2',
        embed_dims=64,
        num_layers=[3, 4, 18, 3],
        init_cfg=dict(checkpoint='https://github.com/whai362/PVT/'
                      'releases/download/v2/pvt_v2_b3.pth')),
    neck=dict(in_channels=[64, 128, 320, 512]))
fp16 = dict(loss_scale=dict(init_scale=512))