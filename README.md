# visualisierung


# Front app
Setup
- npm install
- npm run serve (To run frontend app)
## Todo
- Determine choices needed in dropdown to be passed to BITES. This can be done in Chart.vue in Front app.

# Back app

Setup
- Move app.py, RGBSG_analyse_plot.py, plot_chart.py, into examples folder
- Move rgbsg.h5 into data/RGBSG folder
- Create a "charts" folder in examples folder
   - move RGBSG_BITES.jpg into charts folder 

- python app.py (To run backend)

## Todo
- Ensure to save all charts needed to be displayed in image format (svg preferred, but png and jpg is fine)

- fix the functions plotting beeswarm charts. they do not work when i tried the file you sent me (function is in plot_chart.py. But to run locally for testing, you can run RGBSG_analyse_plot.py)
