import json
import os
import pyautogui as pyag
import keyboard as kb
import pyperclip as pc
import easyocr as eor
if __name__ == '__main__':
    def ocr():
        pyag.screenshot(region=[config['lt'][0], config['lt'][1], config['rd']
                        [0]-config['lt'][0], config['rd'][1]-config['lt'][1]]).save('region.png')
        reader = eor.Reader(['ch_sim', 'en'], gpu=True)
        pc.copy(reader.readtext('region.png', detail=0)[0])
        print('success!')

    def set_lt():
        config['lt'] = pyag.position()
        json.dump(config, open('config.json', 'w', encoding='utf8'))

    def set_rd():
        config['rd'] = pyag.position()
        json.dump(config, open('config.json', 'w', encoding='utf8'))
    if not os.path.exists('config.json'):
        config = {'lt': None, 'rd': None}
    else:
        config = json.load(open('config.json', 'r', encoding='utf8'))
    print('f1:识别')
    print('f2:设置左上角坐标')
    print('f3:设置右下角坐标')
    kb.add_hotkey('f1', ocr)
    kb.add_hotkey('f2', set_lt)
    kb.add_hotkey('f3', set_rd)
    kb.wait('f8')
