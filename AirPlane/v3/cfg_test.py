import configparser

# 第一步生成
cfg = configparser.ConfigParser()

cfg.read("cfg_test.py")

sp_name = cfg.get("SmallPlane", "name")
print(sp_name)
sp_width = cfg.getint("SmallPlane", "width")
print(sp_width)
print(type(sp_width))

