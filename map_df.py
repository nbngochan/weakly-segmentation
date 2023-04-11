import os
import pandas as pd

annotation_path = 'D:/lab/dataset/HelloAppleWorld/Yolo-type/Label'
image_dir = 'D:/lab/dataset/HelloAppleWorld/Yolo-type/Image'
annotation_dict = {'image_id': [], 'image_path': [],
                   'cx': [], 'cy': [],
                   'rw': [], 'rh': [],
                   'label': []}

# annotation information
for annotation in os.listdir(annotation_path):
    file_path = os.path.join(annotation_path, annotation)
    file = open(file_path, 'r')
    lines = file.readlines()

    for line in lines:
        data = line.strip().split(' ')

        image_id = os.path.basename(file_path).split('.')[0]
        image_path = os.path.join(image_dir, f'{image_id}.jpg').replace('\\', '/')

        annotation_dict['image_id'].append(image_id)
        annotation_dict['image_path'].append(image_path)
        annotation_dict['cx'].append(data[1])
        annotation_dict['cy'].append(data[2])
        annotation_dict['rw'].append(data[3])
        annotation_dict['rh'].append(data[4])
        annotation_dict['label'].append(data[0])


annotation_df = pd.DataFrame(annotation_dict, columns=['image_id', 'image_path', 'cx', 'cy', 'rw', 'rh', 'label'])


annotation_df.to_csv('annotation_df.csv', index=False)
