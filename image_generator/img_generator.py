import sys

try:
    import mapnik
except:
    print '\n\nThe mapnik library and python bindings must have been compiled and \
installed successfully before running this script.\n\n'
    sys.exit(1)


class IBuilderImage:
    spatialReference = {4674: "+proj=longlat +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +no_defs ",
                             4618:"+proj=longlat +ellps=aust_SA +towgs84=-67.35,3.88,-38.22,0,0,0,0 +no_defs",
                             9999:"+proj=lcc +ellps=GRS80 +lat_0=49 +lon_0=-95 +lat+1=49 +lat_2=77 +datum=NAD83 +units=m +no_defs"
    }

    def __init__(self, layer, bbox=0, srs=4674, width=800, height=600):
        self.geometry = layer['geometry']
        self.style = layer['style']
        self.bbox = bbox
        self.srs = srs
        self.width = width
        self.height = height
        self.imgType = 0
        self.mapnikObj = mapnik.Map(width, height)
        self.mapnikImg = mapnik.Image(width, height)

    def generate(self):
        pass

#builderPNG, builderJpeg, builderTiff

class BuilderPNG(IBuilderImage):
    def __init__(self, layer, bbox=0, srs=4674, width=800, height=600):
        IBuilderImage.__init__(self, layer)
        self.imgType = "PNG"

    def generate(self):

        # Set the initial extent
        # see envelope() function of mapnik
        self.mapnikObj.background = mapnik.Color('white')
        mapnik.load_map(self.mapnikObj, self.style)
        self.layer = mapnik.Layer('Provinces')
        self.layer.srs =self.spatialReference[self.srs]
        self.layer.datasource = mapnik.Shapefile(file=self.geometry, encoding='latin1')
        self.layer.styles.append("provinces")
        self.mapnikObj.layers.append(self.layer)

        if self.bbox==0:
            self.mapnikObj.zoom_all()

        # Render map
        mapnik.render(self.mapnikObj, self.mapnikImg)

        # Save image to files
        self.mapnikImg.save('test.png', 'png')  # true-colour RGBA