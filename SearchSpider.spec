# -*- mode: python -*-
a = Analysis(['SearchSpider.py'],
             pathex=['E:\\workspace\\GitHub\\SearchSpider'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SearchSpider.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
