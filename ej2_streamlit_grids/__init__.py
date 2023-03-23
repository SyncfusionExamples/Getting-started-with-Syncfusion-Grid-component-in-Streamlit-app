import os
import streamlit.components.v1 as components
import pandas as pd
import json
import typing


_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "EJ2Grid",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("EJ2Grid", path=build_dir)

def GridComponent (props: typing.Dict):
    """Create a new instance of "EJ2Grid".

    Parameters
    ----------
    data: pd.DataFrame
        The data stream of the CSV file that contains the data to be displayed on the Grid view.
    settings: Dict or typing.Dict
        An optional parameter that enables additional features to the Grid component.
    theme: string
        An optional parameter that changes the theme of the Grid component. It is in Material theme by default.

    """


    # Stores the JSON dataset that should be passed to the Front-end.
    dataSet = PdToJson(props._GridProps__dataSource)
    params ={
                # Properties
                'data': dataSet,
                'allowExcelExport': props.allowExcelExport,
                'allowFiltering': props.allowFiltering,
                'allowGrouping': props.allowGrouping,
                'allowMultiSorting': props.allowMultiSorting,
                'allowKeyboard': props.allowKeyboard,
                'allowPaging': props.allowPaging,
                'allowPdfExport': props.allowPdfExport,
                'allowReordering': props.allowReordering,
                'allowResizing': props.allowResizing,
                'allowRowDragAndDrop': props.allowRowDragAndDrop,
                'allowSelection': props.allowSelection,
                'allowSorting': props.allowSorting,
                'allowTextWrap': props.allowTextWrap,
                'enableAdaptiveUI': props.enableAdaptiveUI,
                'enableColumnVirtualization': props.enableColumnVirtualization,
                'enableHeaderFocus': props.enableHeaderFocus,
                'enableHover': props.enableHover,
                'enableImmutableMode': props.enableImmutableMode,
                'enableInfiniteScrolling': props.enableInfiniteScrolling,
                'enablePersistence': props.enablePersistence,
                'enableStickyHeader': props.enableStickyHeader,
                'enableVirtualMaskRow': props.enableVirtualMaskRow,
                'enableVirtualization': props.enableVirtualization,
                'enableStickyHeader': props.enableStickyHeader,
                'showColumnChooser': props.showColumnChooser,
                'showColumnMenu': props.showColumnMenu,
                'toolbarItems': props.toolbarItems,
                'childGrid': props.childGrid,
                'columnDirective': props.columnDirective,
                'editSettings': props.editSettings,
                'rowCount': props.rowCount,
                'sortSettings': props.sortSettings,
                'filterSettings': props.filterSettings,
                'groupSettings': props.groupSettings,
                'pageSettings': props.pageSettings,
                'infiniteScrollSettings': props.infiniteScrollSettings,
                'textWrapSettings': props.textWrapSettings,
                'licenseKey': props._GridProps__license_key,
                'height': props.height,
                'width': props.width,
                'rowHeight': props.rowHeight,
                'rowRenderingMode': props.rowRenderingMode,
                'selectedRowIndex': props.selectedRowIndex,
                'searchSettings': props.searchSettings,
                'selectionSettings': props.selectionSettings,
                'printMode': props.printMode,
                'frozenColumns': props.frozenColumns,
                'gridLines': props.gridLines,
                'frozenRows': props.frozenRows,
                'theme': props.theme,

            }
    component_value = _component_func(params=params)

def PdToJson(dataframe: pd.DataFrame):
    """Converts the Pandas dataframe to the JSON object.

    Parameters
    ----------
    dataframe: pd.DataFrame
        The data stream of the CSV file that contains the data to be displayed on the Grid view.

    Returns
    -------
    json_list: JSON.object
        The JSON variable which holds the object of data.
    """
    json_obj = json.loads(dataframe.to_json())
    dict_keys = list(json_obj.keys())
    json_list = []

    for index in range(len(json_obj[dict_keys[0]])):
        row_obj = dict()
        for column in dict_keys:
            row_obj[column] = json_obj[column][str(index)]
        json_list.append(row_obj)
        
    return json_list

class GridProps:
    
    def __init__(self, dataSource: pd.DataFrame):
        self.__dataSource = dataSource
        self.allowExcelExport = False
        self.allowFiltering = False
        self.allowGrouping = False
        self.allowKeyboard = True
        self.allowMultiSorting = False
        self.allowPaging = False
        self.allowPdfExport = False
        self.allowReordering = False
        self.allowResizing = False
        self.allowRowDragAndDrop = False
        self.allowSelection = True
        self.allowSorting = False
        self.allowTextWrap = False
        self.enableAdaptiveUI = False
        self.enableColumnVirtualization = False
        self.enableHeaderFocus = False
        self.enableHover = True
        self.enableImmutableMode = False
        self.enableInfiniteScrolling = False
        self.enablePersistence = False
        self.enableRtl = False
        self.enableStickyHeader = False
        self.enableVirtualMaskRow = True
        self.enableVirtualization = False
        self.showColumnChooser = False
        self.showColumnMenu = False
        self.toolbarItems = None
        self.childGrid = None
        self.columnDirective = None
        self.rowCount = None
        self.sortSettings = {}
        self.pageSettings = {}
        self.filterSettings = {}
        self.groupSettings = {}
        self.searchSettings = {}
        self.selectionSettings = {}
        self.infiniteScrollSettings = {}
        self.textWrapSettings = {}
        self.height = 'auto'
        self.width = 'auto'
        self.rowHeight = None
        self.rowRenderingMode = None
        self.selectedRowIndex = None
        self.printMode = None
        self.frozenColumns = None
        self.frozenRows = None
        self.gridLines = None
        self.editSettings = None
        self.theme = 'material'
        self.__license_key = None

    def registerLicense(self, key: str):
        self.__license_key = key

