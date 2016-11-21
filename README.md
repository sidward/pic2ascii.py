# pic2ascii.py

A simple python hack to print ascii images from image files. An example result can be seen [here](https://raw.githubusercontent.com/sidward/pic2ascii.py/master/result.txt).

## Getting started

Clone the repository into the desired directory.

```
cd <dir>
git clone https://github.com/sidward/pic2ascii.py
cd pic2ascii.py
```

Optionally, add an alias so that you can call this function from anywhere. 

```
echo 'alias pic2ascii.py="exec <dir>/pic2ascii.py"' >> ~/.bash_aliases
```

## Prerequisites

This requires ```numpy``` and ```scipy```.

## Usage

Assuming the bash alias has been added, 

```
pic2ascii.py <path to picture>
```

Alternatively,
```
pic2ascii.py <path to picture> > out.txt
```

See ```example.sh``` for a sample call.

## License 

This project is licensed under the MIT License - see the [LICENSE.md](License.md) file for details
