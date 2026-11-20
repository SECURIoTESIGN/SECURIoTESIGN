# SecD4CLOUDMOBILE-ML

Machine Learning Implementation into SecD4CLOUDMOBILE framework used to Assessing the Training of Machine Learning Models Using the Tools to discusses the potential substitution of the coded five tools of the secD4CloudMobile framework by AI models and presents some of the results from experiments performed to assess this possibility. The present application in its version 1.0 is a framework of tools whose main purpose is to ensure security and privacy by design software for the cloud, mobile, and IoT ecosystem. It allows generating reports (security requirements, good practices, security mechanisms, mapping attack models and specifying security tests and automation tools) according to the user request based on responses to a questionnaire by the user.

SecD4CLOUDMOBILE-ML was developed by Francisco T. Chimuco and Pedro R. M. Inácio from the Instituto de Telecomunicações, and Department of Computer Science, Universidade da Beira Interior, Covilhã, Portugal.

Copyright (c) 2024 Francisco T. Chimuco and Pedro R. M. Inácio francisco.chimuco@ubi.pt. All rights reserved.

SPDX-License-Identifier: Apache-2.0. The copy of the License may be obtained at http://www.apache.org/licenses/LICENSE-2.0

## 1. Project Download

Due to the substantial volume of dataset files and training assets, the complete repository is hosted on OneDrive and can be downloaded via the following link:

* **OneDrive Direct Download:** [Download SecD4CLOUDMOBILE-ML](https://ubipt-my.sharepoint.com/:f:/g/personal/francisco_chimuco_ubi_pt/IgBSKvXRytDgR5jbUBo5lJI0AZI3s1Jm_bfmePb9fAE-zGg?e=T7v6X2)

Once downloaded, extract the archive and navigate to the project root directory (`SAM-ML-main`).

## 2. System Prerequisites

* **Python:** Python 3.10 to 3.12 (Python 3.12 recommended)

* **Database Engine:** MySQL 8.0+ or MariaDB 10.6+ (local or remote instance)

* **Package Manager:** `pip` (upgraded to the latest version)

## 3. Environment Isolation (Recommended)

To ensure reproducible experimental conditions and avoid package dependency conflicts across operating systems (macOS, Linux, or Windows), isolate the project using a virtual environment.

### macOS / Linux

```
cd SAM-ML-main
python3.12 -m venv .venv
source .venv/bin/activate

```

### Windows (PowerShell)

```
cd SAM-ML-main
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1

```

Upgrade `pip` within the active environment:

```
python -m pip install --upgrade pip

```

## 4. Dependency Installation

With the virtual environment active, install all required Python libraries via `requirements.txt`:

```
pip install -r requirements.txt

```

*(Note: The framework utilizes `mysql-connector-python` by default to avoid native C-compiler header dependencies on macOS and Windows).*

## 5. System-Level C Dependencies (Optional: `mysqlclient`)

If your deployment setup specifically requires the native C-backed `mysqlclient` interface (`import MySQLdb`) rather than `mysql-connector-python`, install the MySQL client headers beforehand:

* **macOS (Homebrew):**

  ```
  brew install mysql-client pkg-config
  export PKG_CONFIG_PATH="$(brew --prefix mysql-client)/lib/pkgconfig"
  export LDFLAGS="-L$(brew --prefix mysql-client)/lib"
  export CPPFLAGS="-I$(brew --prefix mysql-client)/include"
  pip install --no-cache-dir mysqlclient
  
  ```

* **Ubuntu / Debian:**

  ```
  sudo apt-get update
  sudo apt-get install -y python3-dev default-libmysqlclient-dev build-essential pkg-config
  pip install --no-cache-dir mysqlclient
  
  ```

* **Fedora / RHEL / CentOS:**

  ```
  sudo dnf install -y python3-devel mysql-devel pkgconfig
  pip install --no-cache-dir mysqlclient
  
  ```

## 6. Database Configuration

1. Verify that your MySQL or MariaDB database server is running.

2. Initialize the target database and import the required schema files.

3. Update database access parameters (host, port, user credentials, database name) in `src/constants/constants.py`.

## 7. Execution and Verification

### Verification of Installed Modules

Execute the following verification command from the project root to ensure all machine learning, dataset transformation, and database packages load without issue:

```
python -c "import mysql.connector, dask.dataframe, pyarrow, arff, imblearn, skmultilearn, community, networkx, matplotlib, requests; print('All framework dependencies verified successfully.')"

```

### Running the Application

Always invoke the main execution script from the **project root directory** (`SAM-ML-main`):

```
python main.py

```

> **Execution Note:** Avoid directly invoking submodule files within `src/` (e.g., `python src/handler/database_handler.py`), as relative package references will raise an `ImportError: attempted relative import with no known parent package`. To run or test a specific module independently, use Python's module flag from the root directory:
>
> ```
> python -m src.handler.database_handler
> 
> ```

## 8. Troubleshooting Common Errors

| Error Symptom | Root Cause | Resolution | 
| ----- | ----- | ----- | 
| `Failed to build 'mysqlclient'` | Missing OS-level MySQL header files | Use `mysql-connector-python` (included in `requirements.txt`) | 
| `No module named 'mysql'` | Mismatched Python interpreter path | Execute `python -m pip install mysql-connector-python` in the active environment | 
| `No module named 'pyarrow'` | Missing Arrow backend for `dask[dataframe]` | Install `pyarrow` (`pip install pyarrow`) | 
| `No module named 'arff'` | PyPI module name mismatch | Install `liac-arff` (`pip install liac-arff`) | 
| `No module named 'community'` | Missing Louvain community detection library | Install `python-louvain` (`pip install python-louvain`) | 
| `attempted relative import with no known parent package` | Direct script invocation from a subdirectory | Run `python main.py` or `python -m src.<module_path>` from root | 

# Acknowledgment

This Work was developed under Doctoral Grant, supported by project CENTRO-01-0145-FEDER-000019 - C4 - Competence Center in Cloud Computing, Research Line 1: Cloud Systems, Work package WP 1.2 - Security by Construction in Cloud and Internet of Things Ecosystems, funded by the 2020 Center, cofinanced by the European Regional Development Fund (ERDF) through the Programa Operacional Regional do Centro (Centro 2020), in the scope of the Sistema de Apoio à Investigação Científica e Tecnológica - Programas Integrados de IC&DT.
