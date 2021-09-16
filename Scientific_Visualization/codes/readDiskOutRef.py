from paraview.simple import *
path = '/Users/razoumov/Documents/workshops/visualization/data/'
reader = ExodusIIReader(FileName=path+'disk_out_ref.ex2')
Show()
Render()
