import pip

def requirement():
    if hasattr(pip, 'main'):
        pip.main(['install', 'pytube'])
        pip.main(['install', 'opencv-python'])
        pip.main(['install', '-r','requirements.txt'])
    else:
        pip._internal.main(['install', 'pytube'])
        pip._internal.main(['install', 'opencv-python'])
        pip._internal.main(['install', '-r','requirements.txt'])