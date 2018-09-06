import os
for root, dirs, files in os.walk("D:/BackupXP/Prot7/BxDoc/VEJA/P2P/SEGDOC/INTIMACOES_DIARIAS", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   '''for name in dirs:
      print(os.path.join(root, name))'''