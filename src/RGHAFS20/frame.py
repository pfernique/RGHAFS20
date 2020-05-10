import vtk
import numpy as np
import os
from tempfile import NamedTemporaryFile
from matplotlib import pyplot as plt
from matplotlib import image as img

def plot_spheres(dataframe, renderer, r=0, g=0, b=0, size=5, **kwargs):
    """
    """

    points = vtk.vtkPoints()
    for x, y, z in zip(dataframe.X, dataframe.Y, dataframe.Z):
        points.InsertNextPoint(x, y, z)

    if points.GetNumberOfPoints() > 0:
        for i in range(points.GetNumberOfPoints()):
            sphereSource = vtk.vtkSphereSource()
            sphereSource.SetRadius(size)
            sphereSource.SetCenter(*np.array(points.GetPoint(i)))
            mapper = vtk.vtkPolyDataMapper()
            if vtk.VTK_MAJOR_VERSION <= 5:
                mapper.SetInput(sphereSource.GetOutput())
            else:
                mapper.SetInputConnection(sphereSource.GetOutputPort())
            pointActor = vtk.vtkActor()
            pointActor.SetMapper(mapper)
            pointActor.GetProperty().SetColor(r,g,b)
            renderer.AddActor(pointActor)
    renderer.ResetCamera()

def plot_delaunay_2D(dataframe, renderer, r=0, g=0, b=0, **kwargs):
    """
    """

    points = vtk.vtkPoints()

    for x, y, z in zip(dataframe.X, dataframe.Y, dataframe.Z):
        points.InsertNextPoint(x, y, z)

    if points.GetNumberOfPoints() > 2:
        polydata = vtk.vtkPolyData()
        polydata.SetPoints(points)
        delaunay2D = vtk.vtkDelaunay2D()
        if vtk.VTK_MAJOR_VERSION <= 5:
            delaunay2D.SetInput(polydata)
        else:
            delaunay2D.SetInputData(polydata)
        delaunayMapper = vtk.vtkDataSetMapper()
        delaunayMapper.SetInputConnection(delaunay2D.GetOutputPort())
        delaunayActor = vtk.vtkActor()
        delaunayActor.SetMapper(delaunayMapper)
        delaunayActor.GetProperty().SetColor(r,g,b)
        renderer.AddActor(delaunayActor)
    renderer.ResetCamera()

def renderers(window, rows=1, cols=1):
    renderer = vtk.vtkRenderer()
    rows = np.linspace(0,1,rows+1)
    cols = np.linspace(0,1,cols+1)
    rows, cols = np.meshgrid(rows, cols)
    renderers = []
    for r, c in zip(range(rows.shape[0]-1), range(cols.shape[1]-1)):
        viewport = rows[r, r], cols[c, c], rows[r+1, r+1], cols[c+1, c+1]
        renderers.append(vtk.vtkRenderer())
        window.AddRenderer(renderers[-1])
        renderers[-1].SetViewport(viewport)
        renderers[-1].SetBackground(1., 1., 1.)
    return renderers

def synchronize(*renderers):
    camera = renderers[0].GetActiveCamera()
    for renderer in renderers:
        renderer.SetActiveCamera(camera)
        renderer.ResetCamera()

def show(window, name=None, magnification=10):
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(window)

    interactor.Initialize()
    window.Render()
    interactor.Start()

    windowToImageFilter = vtk.vtkWindowToImageFilter()
    windowToImageFilter.SetInput(window)
    windowToImageFilter.setScale(magnification)
    windowToImageFilter.SetInputBufferTypeToRGBA()
    windowToImageFilter.ReadFrontBufferOff()
    windowToImageFilter.Update()
    writer = vtk.vtkPNGWriter()
    if name is None:
        filehandler = NamedTemporaryFile(delete=False)
    else:
        filehandler = open(name, 'w')
    writer.SetFileName(filehandler.name)
    writer.SetInputConnection(windowToImageFilter.GetOutputPort())
    writer.Write()
    window.Finalize()
    interactor.TerminateApp()
    del interactor
    axes = plt.subplot()
    axes.imshow(img.imread(filehandler.name))
    axes.axis('off')
    if name is None:
        os.unlink(filehandler.name)
