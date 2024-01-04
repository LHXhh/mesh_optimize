"""
将colmap的cameras.txt中的SIMPLE_RADIAL改为PINHOLE
"""

def convert_to_pinhole(model_params):
    ## 提取每一个SIMPLE_RADIAL参数
    list_name, model_type, width, height, distortion_param, cx, cy, _ = model_params.split()
    model_type = "PINHOLE"  ## 更新相机模型
    
    ## 创建PINHOLE参数
    pinhold_parama = f'{list_name} {model_type} {width} {height} {distortion_param} {distortion_param} {cx} {cy}'
    
    return pinhold_parama

def update_camera_model(input_file, output_file):
    ## 读取文件内容并存储在列表
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    file.close()
    
    ## 按行处理
    for i in range(len(lines)):
        if 'SIMPLE_RADIAL' in lines[i]:
            lines[i] = convert_to_pinhole(lines[i]) + '\n'
            
    ## 更新文件
    with open(output_file, 'w') as file:
        file.writelines(lines)
    
    file.close()

## 输入文件和输出文件
input_filename = "./sparse/1/cameras.txt"
output_filename = "./sparse/1/cameras_pinhole.txt"

## 更新相机模型
update_camera_model(input_filename, output_filename)