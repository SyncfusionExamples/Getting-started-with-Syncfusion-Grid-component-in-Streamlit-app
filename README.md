# Getting Started with the Syncfusion Grid component in the Streamlit Application

This article provides a step-by-step guide for setting up a [Streamlit](https://streamlit.io/) application with a Python environment and integrating the Syncfusion Grid components.

`Streamlit` is a free and open-source framework that enables quick development and sharing of visually appealing web applications for machine learning and data science.

## Setting up the Streamlit application

To begin working with the Streamlit framework, it is recommended to create a Python environment using [venv](https://docs.python.org/3/library/venv.html). Refer to the below command to create a new Python environment:

```bash
python -m venv my-app
```

Upon completing the aforementioned step to create **my-app**, run the following command to install Streamlit:

```bash
cd my-app
pip install streamlit
```

Now that **my-app** is ready to run with default settings, let's add Syncfusion Grid component to the application.

## Add the Syncfusion Grid package

Install the Syncfusion Grid component package from [PyPI](https://pypi.org/project/ej2-streamlit-grids/) by executing the following command:

```sh
pip install ej2-streamlit-grids
```

## Add the Syncfusion Grid component

Follow the below steps to add the Syncfusion Grid component to the Streamlit application:

1\. Create a Python file named **demo.py** and import the Grid component (`SfGrid`) into the file:

```py
from ej2_streamlit_grids import SfGrid, GridProps
```

2\. Create a `CSV` file named **dataset.csv** and populate it with data in the following format:

```sh
OrderID, CustomerName, OrderDate, Freight, ShippedDate, ShipCountry
10248, Paul Henriot, 7/4/1996, $32.38, 7/16/1996, France
10249, Karin Josephs, 7/5/1996, $11.61, 7/10/1996, Germany
10250, Mario Pontes, 7/8/1996, $65.83, 7/12/1996, Brazil
10251, Mary Saveley, 7/8/1996, $41.34, 7/15/1996, France
```

3\. Read the data from the `CSV` file and initialize the `GridProps` object:

```py
data = pd.read_csv('dataset.csv')
props = GridProps(data)

SfGrid(props)
```

## Import Syncfusion CSS styles

You can import themes for the Syncfusion Streamlit component from the CDN. Refer to the [themes topic](https://ej2.syncfusion.com/react/documentation/appearance/theme/) to learn more about built-in themes. The `Material` theme is the default theme for the Streamlit Grid component.

You can change the default theme with any of the available [built-in themes](https://ej2.syncfusion.com/react/documentation/appearance/theme/). In this article, the `Fluent` theme is applied using `theme` property, which are available in CDN. The necessary `Fluent` CSS styles for the Grid component were passed into the `theme` property, which is referenced using the code snippet below.

```py
props.theme = 'https://cdn.syncfusion.com/ej2/22.1.34/fluent.css'
```

## Run the application

Here is the summarized code for the above steps in the **demo.py** file:

```py
from ej2_streamlit_grids import SfGrid, GridProps
import pandas as pd

data = pd.read_csv('dataset.csv')
props = GridProps(data)
props.theme = 'https://cdn.syncfusion.com/ej2/22.1.34/fluent.css'

SfGrid(props)
```

Ensure that terminal is in the correct project directory where **demo.py** is located. Run the application using the following command:

```sh
streamlit run demo.py
```

The output will appear as follows:

![demo](images/ej2_streamlit_grids_demo.png)

## Grid features demo

The Grid component is rendered along with some additional features in the **demo.py** file located in the **demos** folder. The resulting output with these features will be displayed as depicted below:

![demo](images/ej2_streamlit_grids_demos.gif)