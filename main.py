import db_connect
import pandas as pds

engine = db_connect.Engine()
engine_conn = engine.db


dataFrame = pds.read_sql("select * from \"pd_data\"", engine_conn)
pds.set_option('display.expand_frame_repr', False)

print(dataFrame)
del engine
