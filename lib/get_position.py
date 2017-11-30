# refer to http://blog.csdn.net/lql0716/article/details/54174293

import cv2
import numpy as np
import config as cfg


def get_position(im, title='get_rect'):
    def onMouse(event, x, y, flags, param):
        if param['stop']:
            param['current_pos'] = param['br']
        else:
            param['current_pos'] = (x, y)

        if event == cv2.EVENT_LBUTTONDOWN:
            if param['tl'] is None:
                param['tl'] = param['current_pos']
            elif param['br'] is None:
                assert param['tl'] is not None
                param['br'] = param['current_pos']
                param['stop'] = True
            else:
                assert param['tl'] is not None
                assert param['br'] is not None
                param['sure'] = True
        elif event == cv2.EVENT_RBUTTONDOWN:
            param['reset'] = True

    while True:
        mouse_params = {'tl': None, 'br': None, 'current_pos': None,
                        'stop': False, 'sure': False, 'reset': False}

        cv2.namedWindow(title)
        cv2.moveWindow(title, 100, 100)
        cv2.setMouseCallback(title, onMouse, mouse_params)
        cv2.imshow(title, im)

        while True:
            im_draw = np.copy(im)

            if mouse_params['tl'] is not None:
                cv2.rectangle(im_draw, mouse_params['tl'],
                    mouse_params['current_pos'], (255, 0, 0), thickness=cfg.thickness)

            cv2.imshow(title, im_draw)
            _ = cv2.waitKey(10)

            if mouse_params['reset'] or mouse_params['sure']:
                break

        if mouse_params['sure']:
            cv2.destroyAllWindows()
            break

    tl = (min(mouse_params['tl'][0], mouse_params['br'][0]),
        min(mouse_params['tl'][1], mouse_params['br'][1]))
    br = (max(mouse_params['tl'][0], mouse_params['br'][0]),
        max(mouse_params['tl'][1], mouse_params['br'][1]))

    # (x1, y1), (x2, y2)
    return (tl, br)
