import  os
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['实现打开子窗口.py','-w','--icon=icon.ico']
    run(opts)
