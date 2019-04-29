import os

train_task_id = 'SIZE384'
initial_epoch = 0
epoch_num = 24
lr = 1e-3
decay = 5e-4
# clipvalue = 0.5  # default 0.5, 0 means no clip
patience = 5
load_weights = True
lambda_inside_score_loss = 4.0
lambda_side_vertex_code_loss = 1.0
lambda_side_vertex_coord_loss = 1.0

total_img = 60000
validation_split_ratio = 0.1
max_train_img_size = int(train_task_id[-3:])
max_predict_img_size = int(train_task_id[-3:])  # 2400
assert max_train_img_size in [256, 384, 512, 640, 736], \
    'max_train_img_size must in [256, 384, 512, 640, 736]'
if max_train_img_size == 256:
    batch_size = 8
elif max_train_img_size == 384:
    batch_size = 8
elif max_train_img_size == 512:
    batch_size = 8
else:
    batch_size = 8
steps_per_epoch = total_img * (1 - validation_split_ratio) // batch_size
validation_steps = total_img * validation_split_ratio // batch_size
csv_path='E:\py_projects\data_new\data_new\data\original_csv\concat_train.csv'
data_dir = 'E:\py_projects\data_new\data_new\data'
origin_image_dir_name = 'train_img'
origin_txt_dir_name = 'train_txt'
train_image_dir_name = 'resized_images'
train_label_dir_name = 'resized_images_labels'
show_gt_image_dir_name = 'show_gt_images'
show_act_image_dir_name = 'show_act_images'
gen_origin_img = True
draw_gt_quad = False
draw_act_quad = False
val_fname = 'val_SIZE256.txt'
train_fname = 'train_SIZE256.txt'
# in paper it's 0.3, maybe to large to this problem
shrink_ratio = 0.2
# pixels between 0.2 and 0.6 are side pixels
shrink_side_ratio = 0.6
epsilon = 1e-4

num_channels = 3
feature_layers_range = range(5, 1, -1)
# feature_layers_range = range(3, 0, -1)
feature_layers_num = len(feature_layers_range)
# pixel_size = 4
pixel_size = 2 ** feature_layers_range[-1]
locked_layers = False

# if not os.path.exists('model'):
#     os.mkdir('model')
# if not os.path.exists('saved_model'):
#     os.mkdir('saved_model')

model_weights_path = 'D:\py_projects\VTD\model\east_model\epoch_weights\weights_%s.{epoch:03d}-{val_loss:.5f}.h5' \
                     % train_task_id
saved_model_file_path = 'D:\py_projects\VTD\model\east_model\saved_model\east_model_%s.h5' % train_task_id
saved_model_weights_file_path = 'D:\py_projects\VTD\model\east_model\saved_model\east_model_weights_%s.h5'\
                                % train_task_id
#pixel_threshold = 0.9
pixel_threshold = 0.7
side_vertex_pixel_threshold = 0.9
trunc_threshold = 0.1
predict_cut_text_line = False
predict_write2txt = True
