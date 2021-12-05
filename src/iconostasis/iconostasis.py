import os
from PIL import Image
from tqdm import tqdm

class Iconostasis(object):
    help = u"izi img app debuilder"
    NEW_FOLDER_NAME = u'_test'

    BG_COLORS = {
        'transparent': (),
        'white': (255, 255, 255),
        'black': (1, 1, 1),
    }

    SIZES = {
        '20': (20, 20),
        '29': (29, 29),
        '40': (40, 40),
        '48': (48, 48),
        '58': (58, 58),
        '60': (60, 60),
        '72': (72, 72),
        '76': (76, 76),
        '80': (80, 80),
        '87': (87, 87),
        '96': (96, 96),
        '120': (120, 120),
        '144': (144, 144),
        '152': (152, 152),
        '167': (167, 167),
        '180': (180, 180),
        '192': (192, 192),
        '216': (216, 216),
        '512': (512, 512),
        '1024': (1024, 1024),
    }

    RESAMPLES_TYPES = [
        # Image.NEAREST,
        # Image.BOX,
        # Image.BILINEAR,
        # Image.HAMMING,
        Image.BICUBIC,
        # Image.LANCZOS,
    ]

    def __init__(self, *args, **options):

        if not args:
            print('Need path for file(s)')
        else:
            with tqdm(total=len(args)*len(self.BG_COLORS)*len(self.SIZES), unit=' icons', desc=f'Make {len(args)*len(self.BG_COLORS)*len(self.SIZES)} icons') as pbar:
                for arg in args:

                    img_origin = Image.open(arg)
                    img_rgba = img_origin.convert('RGBA')

                    rooot = os.getcwd()
                    _tmp_dirs = img_origin.filename.split('/')
                    _tmp_img_type = ''
                    if _tmp_dirs:
                        _tmp_img_type = _tmp_dirs[-1].split('.')[1]
                        _tmp_dirs[-1] = 'iconostasis_%s' % _tmp_dirs[-1].split('.')[0]
                    result_dir_path = os.path.join(*[rooot] + [_tmp_dirs[-1].replace('.', '')])
                    
                    try:
                        if not os.path.isdir(result_dir_path):
                            os.mkdir(result_dir_path)
                    except Exception as e:
                        pass

                    # print(result_dir_path)
                    if os.path.isdir(result_dir_path):
                        pbar.write(result_dir_path)
                        for bg_color_name, bg_colors_actiom in self.BG_COLORS.items():
                            # pbar.update(1)
                            _tmp_bg_color_dirname = os.path.join(result_dir_path, bg_color_name)
                            try:
                                if not os.path.isdir(_tmp_bg_color_dirname):
                                    os.mkdir(_tmp_bg_color_dirname)
                            except Exception as e:
                                pass
                            for size_name, size_tuple in self.SIZES.items():
                                for restype in self.RESAMPLES_TYPES:
                                    pbar.update(1)
                                    output_origin = img_origin.resize(size_tuple, resample=restype)
                                    output_rgba = img_rgba.resize(size_tuple, resample=restype)
                                    if bg_colors_actiom:
                                        newImage = []
                                        for item in output_rgba.getdata():
                                            if item[:3] == (0, 0, 0) or item[3] < 240:
                                                newImage.append(bg_colors_actiom)
                                            else:
                                                newImage.append(item)
                                        output_rgba.putdata(newImage)
                                        _output_rgba = output_rgba.convert('RGB')
                                        _output_rgba.save(os.path.join(_tmp_bg_color_dirname, '%s_%s_%s.%s' % (_tmp_dirs[-1], size_name, '%s'.split('.')[0] % restype, _tmp_img_type)))
                                    else:
                                        output_origin.save(os.path.join(_tmp_bg_color_dirname, '%s_%s_%s.%s' % (_tmp_dirs[-1], size_name, '%s'.split('.')[0] % restype, _tmp_img_type)))
                            # print(_tmp_bg_color_dirname)
