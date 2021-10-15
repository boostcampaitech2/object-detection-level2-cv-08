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
        num_layers=[2, 2, 2, 2],
        init_cfg=dict(checkpoint='https://github.com/whai362/PVT/'
                      'releases/download/v2/pvt_v2_b1.pth')),
    neck=dict(in_channels=[64, 128, 320, 512]))