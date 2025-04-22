import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from shapely.geometry import Point
from src.utils.settings import Settings
from src.utils.constants import HOVER_BUFFER_SIZE, CLICK_BUFFER_SIZE, DEFAULT_FIGURE_SIZE

class MapManager:
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.settings = Settings.get_instance()
        
        # Create figure and canvas
        self.figure, self.ax = plt.subplots(figsize=DEFAULT_FIGURE_SIZE)
        self.ax.axis('off')
        self.canvas = FigureCanvas(self.figure)
        
        # Initialize map elements
        self.current_state = None
        self.current_dam = None
        self.current_grid_points = []
        self.hover_text = None
        self.info_ax = None
        self.info_box = None

    def plot_state(self, state_name):
        """Plot a state and its dams"""
        if state_name == "STATE":
            return

        self.current_state = state_name
        self.ax.clear()
        
        # Get state boundary and dams
        state_boundary = self.data_manager.get_state_boundary(state_name)
        state_dams = self.data_manager.get_state_dams(state_name)
        
        if state_boundary is not None:
            self.ax.plot(*state_boundary.geometry.exterior.xy, color='black')
        
        if state_dams is not None:
            for _, dam in state_dams.iterrows():
                self.ax.plot(dam.geometry.x, dam.geometry.y, 'ro', markersize=5)
        
        self.ax.axis('equal')
        self.canvas.draw()

    def plot_dam_info(self, dam):
        """Add information box for selected dam"""
        if self.info_ax is not None:
            self.info_ax.remove()
        if self.info_box is not None:
            self.info_box.remove()

        # Create new info plot in bottom right corner with box
        self.info_ax = self.figure.add_axes([0.75, 0.01, 0.3, 0.25])
        self.info_ax.axis('off')

        info_text = f"Dam Name: {dam['dm_name']}\n" \
                   f"Location: ({dam.dm_long}, {dam.dm_lat})"

        # Add text with background box
        bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1.5)
        self.info_ax.text(0.5, 0.5, info_text, 
                         verticalalignment='center', 
                         horizontalalignment='center',
                         transform=self.info_ax.transAxes, 
                         bbox=bbox_props, 
                         wrap=True, 
                         fontsize=10)

        self.canvas.draw()

    def plot_grid_points(self, dam_name):
        """Plot grid points for a selected dam"""
        # Clear existing grid points
        if self.current_grid_points:
            for point in self.current_grid_points:
                point.remove()
            self.current_grid_points = []

        # Get dam and corresponding grid points
        dam = self.data_manager.get_dam_by_name(dam_name)
        if dam is None:
            return

        grid_points = self.data_manager.get_state_grid_points(dam['STATE'])
        if grid_points is not None:
            x = grid_points.geometry.x
            y = grid_points.geometry.y
            self.current_grid_points = self.ax.plot(x, y, 'o', 
                                                  markersize=0.5, 
                                                  color='blue')
            self.canvas.draw()

    def handle_hover(self, event):
        """Handle mouse hover events"""
        if event.inaxes != self.ax:
            return

        x, y = event.xdata, event.ydata
        hover_point = Point(x, y)
        hover_buffer = hover_point.buffer(HOVER_BUFFER_SIZE)

        # Remove existing hover text
        if self.hover_text is not None:
            self.hover_text.remove()
            self.hover_text = None

        # Check if hovering over a dam
        if self.data_manager.dams is not None:
            for _, dam in self.data_manager.dams.iterrows():
                if dam.geometry.intersects(hover_buffer):
                    self.hover_text = self.ax.text(x, y, dam['dm_name'], 
                                                 fontsize=12, 
                                                 color='blue')
                    break
        
        self.canvas.draw()

    def handle_click(self, x, y):
        """Handle mouse click events"""
        click_point = Point(x, y)
        click_buffer = click_point.buffer(CLICK_BUFFER_SIZE)
        
        if self.data_manager.dams is not None:
            for _, dam in self.data_manager.dams.iterrows():
                if dam.geometry.intersects(click_buffer):
                    self.current_dam = dam
                    self.plot_dam_info(dam)
                    self.plot_grid_points(dam['dm_name'])
                    return dam
        
        return None

    def save_map_snapshot(self, filepath):
        """Save current map view as an image"""
        self.canvas.draw()
        self.canvas.print_figure(filepath, dpi=300, bbox_inches='tight')
