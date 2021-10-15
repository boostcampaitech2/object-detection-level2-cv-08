checkpoint_config = dict(interval=1, max_keep_ckpts=5)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
        dict(type='WandbLoggerHook',init_kwargs=dict(project='recycle_trash_OD',name="cascade_rcnn_r50_fpn_PVTv2_b3_custom_fullaug"))
    ])
# yapf:enable
custom_hooks = [dict(type='NumClassCheckHook')]

dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]
