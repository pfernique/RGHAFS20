def plot_points(X, Y, Z, r, g, b, renderer, size=5, **kwargs):
    """
    """

    points = vtk.vtkPoints()
    for x, y, z in zip(X, Y, Z):
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

def plot_delaunay_2D(X, Y, Z, r, g, b, renderer, **kwargs):
    """
    """

    points = vtk.vtkPoints()
    for x, y, z in zip(X, Y, Z):
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
