import cv2
import os
from lib.utils import make_dir
from lib.get_position import get_position


# =============================================================
src_dir = 'source_2_level/'
dst_dir = 'dst/'
done_dir = 'done/'
record_file = 'record_2_level.txt'

make_dir(dst_dir)
make_dir(done_dir)


# =============================================================
sub_dir_list = os.listdir(src_dir)
for pig_id in range(len(sub_dir_list)):
    pig_dst_dir = os.path.join(dst_dir, str(pig_id+1))
    pig_done_dir = os.path.join(done_dir, str(pig_id + 1))

    make_dir(pig_dst_dir)
    make_dir(pig_done_dir)

print('=' * 50)
# =============================================================

for sub_dir in sub_dir_list:
    sub_src_dir = os.path.join(src_dir, str(sub_dir))
    sub_dst_dir = os.path.join(dst_dir, str(sub_dir))
    sub_done_dir = os.path.join(done_dir, str(sub_dir))

    pig_img_list = os.listdir(sub_src_dir)

    for pig_img_name in pig_img_list:
        src_img_path = os.path.join(sub_src_dir, pig_img_name)
        dst_img_path = os.path.join(sub_dst_dir, pig_img_name)
        done_img_path = os.path.join(sub_done_dir, pig_img_name)

        src_img = cv2.imread(src_img_path)
        (a,b) = get_position(src_img, src_img_path)
        dst_img = src_img[a[1]:b[1], a[0]:b[0]]

        # print('(%d, %d), (%d %d)' % (a[1], b[1], a[0], b[0]))
        with open(record_file, 'a') as fp:
            # (x1, y1), (x2, y2)
            fp.write('%s %s %d %d %d %d\n' % (sub_dir, pig_img_name, a[1], b[1], a[0], b[0]))

        print('1.Save crop to [%s].' % dst_img_path)
        # cv2.imwrite(dst_img_path, dst_img)
        print('2.Move [%s] to [%s].' % (src_img_path, done_img_path))
        # os.rename(src_img_path, done_img_path)
        print('=' * 50)
