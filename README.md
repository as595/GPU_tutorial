# GPU_tutorial

---

### Get the code

In your working directory you should clone this repository:

``
git clone https://github.com/as595/GPU_tutorial.git
``

---

### Setting up your environment

I like to use [virtualenv](https://pypi.org/project/virtualenv/) to make sure I'm running in a well-defined environment. 

To create a clean Python3 virtual environment:

``
virtualenv --no-site-packages -p python3 p3env
``

then activate it:

``
source p3env/bin/activate
``

You can then install all of the libraries for these tutorials using:

``
pip3 install -r requirements.txt
``

---

### Launch the notebook using port forwarding

In the terminal launch the notebook using:

``
jupyter notebook --no-browser --port=8888
``

On your laptop forward the port:

``
ssh -N -f -L localhost:8889:localhost:8888 userid@hepgpuX.blackett.manchester.ac.uk
``

You can then open the notebook in the browser on your laptop by copying 

``
http://localhost:8889/?token=xxxxxxxxxxxxxxxxxxxxxxxxxx
``

into the address bar. The token will be displayed in the remote terminal. 


When you're finished you should kill the process that is listening on port 8889. You can find the pid on Mac OSX using:

``
lsof -n -i4TCP:8889 | grep LISTEN
``

or on Linux using:

``
netstat -ntlp | grep 8889
``

