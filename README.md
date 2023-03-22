# Getting started with Syncfusion Grid component in Streamlit application

Developers can write `JavaScript` and `HTML components` that can be rendered in Streamlit apps. Streamlit Components can receive data from, and also send data to, Streamlit Python scripts.

Streamlit Components let you expand the functionality provided in the base Streamlit package. Use Streamlit Components to create the needed functionality for your use-case, then wrap it up in a Python package and share with the broader Streamlit community!

## Installation

To Install streamlit on the local machine follow the [Installation](https://docs.streamlit.io/library/get-started/installation) steps on the official streamlit site.

The Packages and application required for rendering components are,

* [Anaconda Navigator](https://docs.anaconda.com/navigator/).

* [Streamlit module](https://pypi.org/project/streamlit/).

* [Node JS ( v10.24.1 )](https://nodejs.org/en/blog/release/v10.24.1/).

* [React JS](https://reactjs.org/docs/getting-started.html) (optional).

## Setup

After the installation of all required packages. Follow the instruction to setup the development environment.

* Clone the Streamlit [component-template](https://github.com/streamlit/component-template) GitHub repository to the local machine.

* Choose the template from the [component-template](https://github.com/streamlit/component-template) repo whether React platform or not and Use the chosen template folder.

* Inside the `template` folder rename the folder `my-component` to the module name that will reflect on the [pipy.org](https://pypi.org/project/pip/).

## Implementation

The implementation needs basic knowledge of the Python programming language.

### Deployment of the JavaScript / HTML component.

* Open the renamed `my-component` folder on a [VS Code](https://code.visualstudio.com/) (or any other `Text-Editor`).

* Install all default dependent packages, use the following command.

```sh
npm install
```
* Install dependent packages for the component using following command
```sh
npm install <package-name> --save
```

* Deploy the component code on the respective `*.tsx` file inside the folder : `my-component / frontend / src`.

> Note: Dynamic data should be passed from the streamlit backend. So, No need to implement the dynamic data on the frontend.

* The gate-way of the component should starts from the `index.tsx` file with streamlit integration. The component should be finally rendered with streamlit.

* Once all the coding were implemented, Run the component on the local server by executing `npm start` command on the Terminal or Command prompt ( CMD ).

### Deployment of Component on the Streamlit.

* After the development server started, open the `my-component` folder on the another window of the [VS Code](https://code.visualstudio.com/) (or any other `Text-Editor`).

* Now open `__init__.py` file, It acts like a constructor for the Python package when the component package get imported, the `__init__.py` file initiated.

* In `__init__.py` file, rename the class name `my_component` that denotes our Component, the constructor holds the parameter which are passed to the `JS` or `HTML` file.

* The Values or Options are passed to the front end by the `_component_func()` as a parameter from here and received at the front-end as `props.args`.

* Can create another python module to implement the Features to the component, which are manipulated at the `__init__.py` file and passes to the component only as a single parameter.

## Support

Product support is available for through following mediums.

* Creating incident in Syncfusion [Direct-Trac](https://www.syncfusion.com/support/directtrac/incidents/?utm_source=npm&utm_medium=listing&utm_campaign=javascript-layout-npm) support system or [Community forum](https://www.syncfusion.com/forums/essential-js2/?utm_source=npm&utm_medium=listing&utm_campaign=javascript-layout-npm).
* New [GitHub issue](https://github.com/syncfusion/ej2-javascript-ui-controls/issues/new/?utm_source=npm&utm_medium=listing&utm_campaign=javascript-layout-npm).
* Ask your query in [Stack Overflow](https://stackoverflow.com/?utm_source=npm&utm_medium=listing&utm_campaign=javascript-layout-npm) with tag `syncfusion` and `ej2`.

## License

Check the license detail [here](https://github.com/syncfusion/ej2-javascript-ui-controls/blob/master/license/?utm_source=npm&utm_medium=listing&utm_campaign=javascript-layout-npm).

## Changelog

Check the changelog [here](https://github.com/syncfusion/ej2-javascript-ui-controls/blob/master/controls/layouts/CHANGELOG.md/?utm_source=npm&utm_medium=listing&utm_campaign=javascript-layout-npm).

Copyright © 2001 - 2023 Syncfusion Inc. All Rights Reserved. The Syncfusion Essential Studio license and copyright applies to this distribution.
