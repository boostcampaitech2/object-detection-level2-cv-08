checkpoint_config = dict(interval=1, max_keep_ckpts=5)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])


# log_config = dict(
#     # _delete_=True,
#     interval=50,
#     hooks=[
#         dict(type="TextLoggerHook"),
#         dict(type="WandbLoggerHook", init_kwargs=dict(project="recycle-object_detection", name="rcnn_hrnetv2_w32")),
#     ],
# )

# yapf:enable
custom_hooks = [dict(type='NumClassCheckHook')]

dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]
seed = 42
