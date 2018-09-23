cd lib
:easy_install pip
pip3.5 install ./wheel-0.29.0-py2.py3-none-any.whl
:pip install --upgrade pip
:pip install ./pip-9.0.1-py2.py3-none-any.whl
easy_install-3.5 pip
pip3.5 install ./numpy-1.12.0+mkl-cp35-cp35m-win_amd64.whl
pip3.5 install ./scipy-0.19.0-cp35-cp35m-win_amd64.whl


:5个matplotlib依赖包,顺序不要改
pip3.5 install ./six-1.10.0-py2.py3-none-any.whl
pip3.5 install ./pytz-2017.2-py2.py3-none-any.whl
pip3.5 install ./cycler-0.10.0-py2.py3-none-any.whl
pip3.5 install ./python_dateutil-2.6.0-py2.py3-none-any.whl
pip3.5 install ./pyparsing-2.2.0-py2.py3-none-any.whl

pip3.5 install ./matplotlib-1.5.3-cp35-cp35m-win_amd64.whl

pip3.5 install ./PyQt4-4.11.4-cp35-cp35m-win_amd64.whl
pip3.5 install ./scikit_learn-0.18.1-cp35-cp35m-win_amd64.whl

pip3.5 install ./Pygments-2.2.0-py2.py3-none-any.whl
pip3.5 install ./configobj-5.0.6-py2.py3-none-any.whl
pip3.5 install ./traits-4.6.0-cp35-cp35m-win_amd64.whl
pip3.5 install ./pyface-5.1.0-py3-none-any.whl
pip3.5 install ./traitsui-5.1.0-py3-none-any.whl
pip3.5 install ./apptools-4.4.0-py3-none-any.whl
pip3.5 install ./VTK-7.1.1-cp35-cp35m-win_amd64.whl

pip3.5 install ./mayavi-4.5.0+vtk71-cp35-cp35m-win_amd64.whl

pip3.5 install ./absl_py-0.2.0-py2.py3-none-any.whl
pip3.5 install ./protobuf-3.5.2-cp35-cp35m-win_amd64.whl

:d:
:cd python3
:cd Lib
:cd site-packages

:md skfeature

:cd /d %~dp0 
:cd lib
:xcopy skfeature D:\python3\Lib\site-packages\skfeature /s/h/e
